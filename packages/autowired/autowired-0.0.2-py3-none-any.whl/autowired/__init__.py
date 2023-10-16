import inspect
import re
from abc import ABC
from dataclasses import dataclass
from functools import cached_property
from types import FunctionType
from typing import TypeVar, Any, Type, Callable, Optional

try:
    # noinspection PyPackageRequirements
    from loguru import logger
except ImportError:
    import logging

    class SimpleLogger:
        def trace(self, msg: str):
            logging.debug(msg)

    logger = SimpleLogger()

_T = TypeVar("_T")


def _camel_to_snake(name: str) -> str:
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def _group_by(key_fn: Callable[[Any], Any], items: list[Any]) -> dict[Any, list[Any]]:
    result = {}
    for item in items:
        key = key_fn(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


@dataclass(frozen=True)
class PropertyInfo:
    name: str
    type: type
    is_cached: bool

    def to_getter(self, obj) -> Callable[[], Any]:
        return lambda: getattr(obj, self.name)


@dataclass(frozen=True)
class Dependency:
    name: str
    type: Type[_T]
    required: bool


Getter = Callable[[], Any]


@dataclass(frozen=True)
class ResolvedDependency:
    name: str
    type: type
    getter: Getter


def get_properties(obj) -> list[PropertyInfo]:
    properties = []
    for name, attr in inspect.getmembers(type(obj)):
        is_cached_property = isinstance(attr, cached_property)
        is_normal_property = isinstance(attr, property)

        if is_cached_property or is_normal_property:
            getter = attr.fget if is_normal_property else attr.func
            prop_type = getter.__annotations__.get("return", None)
            properties.append(PropertyInfo(name, prop_type, is_cached_property))

    return properties


def is_required(param: inspect.Parameter) -> bool:
    return param.default == inspect.Parameter.empty


def get_dependencies(t: type[_T]) -> list[Dependency]:
    # inspect __init__ method for names and types of parameters
    if "__init__" in t.__dict__:
        init = t.__init__
        if isinstance(init, FunctionType):
            sig = inspect.signature(init)
            return [
                Dependency(name, param.annotation, is_required(param))
                for name, param in sig.parameters.items()
                if name != "self"
            ]
    return []


class DependencyError(Exception, ABC):
    pass


class NotInstantiableException(DependencyError):
    pass


class AmbiguousDependencyException(DependencyError):
    pass


class UnresolvableDependencyException(DependencyError):
    pass


class InitializationError(DependencyError):
    pass


def permit_auto_wire(t: type[_T]) -> bool:
    root_module = t.__module__.split(".")[0]

    if root_module in ["builtins", "typing", "dataclasses", "abc"]:
        return False

    return True


class Container:
    _resolved: list[ResolvedDependency]

    def __init__(self, parent: "Container" = None):
        self._resolved = []
        if parent:
            self._resolved.extend(parent._resolved)

    def get_existing(
        self, t: type[_T], dependency: Dependency
    ) -> ResolvedDependency | None:
        candidates = []
        for r in self._resolved:
            if issubclass(r.type, dependency.type):
                candidates.append(r)

        if len(candidates) == 1:
            return candidates[0]
        if len(candidates) > 1:
            by_name = _group_by(lambda obj: obj.name, candidates)
            if dependency.name in by_name and len(by_name[dependency.name]) == 1:
                return by_name[dependency.name][0]
            else:
                raise AmbiguousDependencyException(
                    f"Failed to resolve dependency {dependency.name} of type {t.__name__}. "
                    f"Multiple candidates found: {candidates}"
                )

        return None

    def unregister_by_name(self, name: str):
        self._resolved = [r for r in self._resolved if r.name != name]

    def register(self, resolved: ResolvedDependency | Any) -> ResolvedDependency:
        if not isinstance(resolved, ResolvedDependency):
            value = resolved
            name = _camel_to_snake(value.__class__.__name__)
            resolved = ResolvedDependency(name, type(value), lambda: value)
        self._resolved.append(resolved)
        return resolved

    def add_context(self, obj: Any, name: str | None = None):
        if name is None:
            name = _camel_to_snake(obj.__class__.__name__)
            self.register(ResolvedDependency(name, type(obj), lambda: obj))

        for prop in get_properties(obj):
            self.register(
                ResolvedDependency(
                    prop.name,
                    prop.type,
                    prop.to_getter(obj),
                )
            )

    def resolve(self, dependency: Dependency | type[_T]) -> _T:
        if not isinstance(dependency, Dependency):
            logger.trace(f"Resolving type {dependency.__name__}")
            dependency = Dependency(
                _camel_to_snake(dependency.__name__), dependency, True
            )

        logger.trace(f"Resolving {dependency}")

        existing = self.get_existing(dependency.type, dependency)
        if existing:
            logger.trace(f"Found existing {existing}")
            return existing.getter()

        logger.trace(f"Existing not found, auto-wiring {dependency}")

        result = self.autowire(dependency.type)

        self.register(
            ResolvedDependency(dependency.name, dependency.type, lambda: result)
        )

        logger.trace(f"Successfully autowired {dependency} to {result}")
        return result

    def autowire(
        self,
        t: type[_T],
        **explicit_kw_args,
    ) -> _T:
        logger.trace(
            f"Auto-wiring {t.__name__} with {len(explicit_kw_args)} explicit args"
        )
        if not permit_auto_wire(t):
            raise NotInstantiableException(
                f"Cannot auto-wire object of type {t.__name__}"
            )

        dependencies = get_dependencies(t)

        resolved_kw_args = dict(explicit_kw_args) if explicit_kw_args else {}

        for dep in dependencies:
            if dep.name in resolved_kw_args:
                continue

            existing = self.get_existing(t, dep)
            if existing:
                resolved_kw_args[dep.name] = existing.getter()
            else:
                try:
                    auto = self.resolve(dep)
                    resolved_kw_args[dep.name] = auto
                except DependencyError as e:
                    if dep.required:
                        raise UnresolvableDependencyException(
                            f"Failed to resolve dependency {dep.name} "
                            f"of type {dep.type.__name__} for {t.__name__}. "
                        ) from e

        try:
            return t(**resolved_kw_args)
        except Exception as e:
            raise InitializationError(f"Failed to initialize {t.__name__}") from e


@dataclass
class _Autowired:
    eager: bool
    kw_args_factory: Callable[[Any], dict[str, Any]]
    explicit_kw_args: dict[str, Any]


def autowired(
    eager: bool = False,
    kw_args_factory: Callable[[], dict[str, Any]] = None,
    **explicit_kw_args,
) -> Any:
    return _Autowired(
        eager=eager, kw_args_factory=kw_args_factory, explicit_kw_args=explicit_kw_args
    )


class ContextMeta(type):
    def __new__(mcs, name, bases, class_dict):
        autowired_fields = {
            key: value
            for key, value in class_dict.items()
            if isinstance(value, _Autowired)
        }

        eager_fields = []
        for field_name, autowired in autowired_fields.items():
            field_type = class_dict.get(f"__annotations__", {}).get(field_name, Any)

            @cached_property
            def autowired_property(self, autowired=autowired) -> field_type:
                explicit_kw_args = (
                    autowired.kw_args_factory(self) if autowired.kw_args_factory else {}
                )
                explicit_kw_args.update(autowired.explicit_kw_args)
                return self.autowire(field_type, **explicit_kw_args)

            class_dict[field_name] = autowired_property
            if autowired.eager:
                eager_fields.append(field_name)

        if eager_fields:

            def new_init(self, *args, **kwargs):
                super(type(self), self).__init__(*args, **kwargs)
                for field_name in eager_fields:
                    getattr(self, field_name)

            class_dict["__init__"] = new_init

        return super().__new__(mcs, name, bases, class_dict)


class Context(metaclass=ContextMeta):
    parent_context: Optional["Context"] = None

    @cached_property
    def container(self) -> Container:
        container = Container(
            self.parent_context.container if self.parent_context else None
        )
        container.add_context(self)
        return container

    def autowire(self, t: type[_T], **explicit_kw_args) -> _T:
        return self.container.autowire(t, **explicit_kw_args)


__all__ = [
    "DependencyError",
    "UnresolvableDependencyException",
    "AmbiguousDependencyException",
    "InitializationError",
    "cached_property",
    "NotInstantiableException",
    "Context",
    "Container",
    "autowired",
]
