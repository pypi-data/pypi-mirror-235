import inspect
import re
from abc import ABC
from dataclasses import dataclass
from functools import cached_property
from types import FunctionType
from typing import TypeVar, Any, Type, Callable

try:
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
class DependencyInfo:
    name: str
    type: Type[_T]
    required: bool


@dataclass(frozen=True)
class PropertyInfo:
    name: str
    type: type
    is_cached: bool

    def to_getter(self, obj) -> Callable[[], Any]:
        return lambda: getattr(obj, self.name)


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


def get_dependencies(t: type[_T]) -> list[DependencyInfo]:
    # inspect __init__ method for names and types of parameters
    if "__init__" in t.__dict__:
        init = t.__init__
        if isinstance(init, FunctionType):
            sig = inspect.signature(init)
            return [
                DependencyInfo(name, param.annotation, is_required(param))
                for name, param in sig.parameters.items()
                if name != "self"
            ]
    return []


class DependencyError(Exception, ABC):
    pass


class NotInstantiableError(DependencyError):
    pass


class AmbiguousDependencyError(DependencyError):
    pass


class UnresolvableDependencyError(DependencyError):
    pass


class InitializationError(DependencyError):
    pass


def permit_auto_wire(t: type[_T]) -> bool:
    if t.__module__ == "builtins":
        return False

    if t.__module__.startswith("typing"):
        return False

    if t.__module__.startswith("dataclasses"):
        return False

    if t.__module__.startswith("abc"):
        return False

    return True


Getter = Callable[[], Any]


@dataclass(frozen=True)
class ResolvedObject:
    name: str
    type: type
    getter: Getter


class Container:
    _resolved: list[ResolvedObject]

    def __init__(self):
        self._resolved = []

    def get_existing(
        self, t: type[_T], dependency: DependencyInfo
    ) -> ResolvedObject | None:
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
                raise AmbiguousDependencyError(
                    f"Failed to resolve dependency {dependency.name} of type {t.__name__}. "
                    f"Multiple candidates found: {candidates}"
                )

        return None

    def replace_existing(self, existing: ResolvedObject, new: ResolvedObject):
        self._resolved.remove(existing)
        self._resolved.append(new)

    def register(self, resolved: ResolvedObject):
        self._resolved.append(resolved)

    def add_context(self, obj: Any, name: str | None = None):
        if name is None:
            name = _camel_to_snake(obj.__class__.__name__)
            self._resolved.append(ResolvedObject(name, type(obj), lambda: obj))

        for prop in get_properties(obj):
            self._resolved.append(
                ResolvedObject(
                    prop.name,
                    prop.type,
                    prop.to_getter(obj),
                )
            )

    def resolve(self, dependency: DependencyInfo | type[_T]) -> _T:
        if not isinstance(dependency, DependencyInfo):
            logger.trace(f"Resolving type {dependency.__name__}")
            dependency = DependencyInfo(
                _camel_to_snake(dependency.__name__), dependency, True
            )

        logger.trace(f"Resolving {dependency}")

        existing = self.get_existing(dependency.type, dependency)
        if existing:
            logger.trace(f"Found existing {existing}")
            return existing.getter()

        logger.trace(f"Existing not found, auto-wiring {dependency}")

        result = self.autowire(dependency.type)

        self._resolved.append(
            ResolvedObject(dependency.name, dependency.type, lambda: result)
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
            raise NotInstantiableError(
                f"Cannot auto-wire object of type {t.__name__} without arguments"
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
                        raise UnresolvableDependencyError(
                            f"Failed to resolve dependency {dep.name} "
                            f"of type {dep.type.__name__} for {t.__name__}. "
                        ) from e

        try:
            return t(**resolved_kw_args)
        except TypeError as e:
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
    @cached_property
    def container(self) -> Container:
        container = Container()
        container.add_context(self)
        return container

    def autowire(self, t: type[_T], **explicit_kw_args) -> _T:
        return self.container.autowire(t, **explicit_kw_args)


__all__ = [
    "DependencyError",
    "UnresolvableDependencyError",
    "AmbiguousDependencyError",
    "InitializationError",
    "cached_property",
    "NotInstantiableError",
    "Context",
    "autowired",
]
