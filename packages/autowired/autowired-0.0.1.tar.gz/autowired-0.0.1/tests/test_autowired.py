from dataclasses import dataclass

from autowired import Context, autowired, cached_property


class SimpleService1:
    def __init__(self):
        import random

        self.id = random.randint(0, 10000000)

    def __str__(self):
        return f"SimpleService1(id={self.id})"

    def __repr__(self):
        return str(self)


@dataclass
class SimpleService2:
    service_one: SimpleService1
    id: int = 0

    def __post_init__(self):
        import random

        self.id = random.randint(0, 10000000)


@dataclass
class SimpleService3:
    service_one: SimpleService1
    service_two: SimpleService2
    id: int = 0
    foo: str = "bar"

    def __post_init__(self):
        import random

        self.id = random.randint(0, 10000000)


class Service1:
    def __init__(self, service2: SimpleService2, blabla: str = "blabla"):
        self.service2 = service2
        self.blabla = blabla

    def __str__(self):
        return f"Service1(service2={self.service2}, blabla={self.blabla})"


class DemoContext(Context):
    service1: Service1 = autowired()

    @cached_property
    def service2(self) -> SimpleService2:
        return self.autowire(SimpleService2)

    @cached_property
    def service3(self) -> SimpleService3:
        return self.autowire(SimpleService3, foo="baz")


if __name__ == "__main__":
    ctx = DemoContext()

    service2 = ctx.service2
    service3 = ctx.service3

    service2b = ctx.service2

    assert id(service2) == id(service2b)
    assert id(service2.service_one) == id(service2b.service_one)
    assert service3.foo == "baz"

    print(service3)
    assert id(service3.service_two) == id(service2)

    print(id(ctx.service2))

    print(ctx.service1)
