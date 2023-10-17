# Autowired

Autowired is a minimalistic dependency injection library for Python, which utilizes type hints to resolve
dependencies.     
It promotes a simple [@cached_property](https://docs.python.org/3/library/functools.html#functools.cached_property)
based singleton pattern to manage dependencies between components.  
Besides that, it provides some tools to make the implementation of that pattern more convenient.

## Installation

```bash
pip install autowired
```

## Basic Example

```python
from autowired import Context, autowired
from dataclasses import dataclass


# Defining application components (e.g. services, controllers, repositories, etc.)

class UserService:
    pass


class AuthService:
    pass


@dataclass
class UserAuthService:
    user_service: UserService
    auth_service: AuthService


@dataclass
class LoginController:
    user_auth_service: UserAuthService

    def login(self, username: str):
        print(f"Logging in user {username} via {self.user_auth_service}")


# Creating a context class to manage the components

class ApplicationContext(Context):
    login_controller: LoginController = autowired()


if __name__ == '__main__':
    ctx = ApplicationContext()
    ctx.login_controller.login("admin")
```

Fields with `=autowired()` and their dependencies are resolved automatically.   
In this example, this means that the `LoginController` as well as all the services are automatically instantiated.    
If that is not desired for some instances, they can also be instantiated manually inside a `cached_property` method.

```python
class CustomUserService(UserService):
    pass


class ApplicationContext(Context):
    login_controller: LoginController = autowired()

    @cached_property
    def user_service(self) -> UserService:
        return CustomUserService()


if __name__ == '__main__':
    ctx = ApplicationContext()
    assert isinstance(ctx.login_controller.user_auth_service.user_service, CustomUserService)
    assert id(ctx.user_service) == id(ctx.login_controller.user_auth_service.user_service)
```

Note that all the actual Components (services, controllers, etc.) are neither aware of the context nor the
existence of the _autowired_ library. They are regular classes, and don't care about how they are instantiated.
Wiring things together is the responsibility of the context only.

Besides dataclasses, you can also use regular classes, as long their `__init__` methods are properly annotated.
Similarly, since the library is completely based on type hints, it is important to specify the correct types not only for the
fields but also for the return types of the `cached_property` methods.

## Example with Settings

```python
from autowired import Context, autowired, cached_property
from dataclasses import dataclass


@dataclass
class UserService:
    db_url: str


@dataclass
class AuthService:
    secret_key: str


@dataclass
class UserAuthService:
    user_service: UserService
    auth_service: AuthService


@dataclass
class LoginController:
    user_auth_service: UserAuthService

    def login(self, username: str):
        print(f"Logging in user {username} via {self.user_auth_service}")


# Create a dataclass to represent your settings
@dataclass
class ApplicationSettings:
    db_url: str
    auth_secret_key: str


# Create a context to manage the components
class ApplicationContext(Context):
    user_auth_service: UserAuthService = autowired()
    login_controller: LoginController = autowired()

    def __init__(self, settings: ApplicationSettings):
        self.settings = settings

    # using cached_property and Context.autowire() to override some of the constructor arguments with values from the settings

    @cached_property
    def user_service(self) -> UserService:
        return self.autowire(UserService, db_url=self.settings.db_url)

    @cached_property
    def auth_service(self) -> AuthService:
        return self.autowire(AuthService, secret_key=self.settings.auth_secret_key)


if __name__ == "__main__":
    # load the settings as desired
    settings = ApplicationSettings("sqlite://database.db", "secret")
    ctx = ApplicationContext(settings=settings)
    ctx.login_controller.login("admin")
```

Following `ApplicationContext` is equivalent to the previous example.

```python
class ApplicationContext(Context):
    user_auth_service: UserAuthService = autowired()
    login_controller: LoginController = autowired()

    def __init__(self, settings: ApplicationSettings):
        self.settings = settings

    # Using the kw_args_factory of the autowired decorator, you can specify a subset of the constructor arguments
    # The remaining arguments are resolved automatically
    user_service: UserService = autowired(
        lambda self: dict(db_url=self.settings.db_url)
    )
    auth_service: AuthService = autowired(
        lambda self: dict(secret_key=self.settings.auth_secret_key)
    )
```

## Scopes / Derived Contexts

```python

# ...

@dataclass
class RequestService:
    user_auth_service: UserAuthService


class RequestContext(Context):
    def __init__(self, parent_context: Context):
        # setting the parent context makes the parent context's beans available
        self.parent_context = parent_context

    request_service: RequestService = autowired()


if __name__ == "__main__":
    root_ctx = ApplicationContext(ApplicationSettings("sqlite://database.db", "secret"))
    request_ctx = RequestContext(root_ctx)

    assert id(root_ctx.user_auth_service) == id(
        request_ctx.request_service.user_auth_service
    )

```

## Advanced Example - FastAPI Application

```python
from dataclasses import dataclass

from fastapi import FastAPI, Request, Depends, HTTPException

from autowired import Context, autowired, cached_property


# Component classes

class DatabaseService:
    def __init__(self, conn_str: str):
        self.conn_str = conn_str

    def load_allowed_tokens(self):
        return ["123", "456"]

    def get_user_name_by_id(self, user_id: int) -> str | None:
        print(f"Loading user {user_id} from database {self.conn_str}")
        d = {1: "John", 2: "Jane"}
        return d.get(user_id)


@dataclass
class UserService:
    db_service: DatabaseService

    def get_user_name_by_id(self, user_id: int) -> str | None:
        if user_id == 0:
            return "admin"
        return self.db_service.get_user_name_by_id(user_id)


@dataclass
class UserController:
    user_service: UserService

    def get_user(self, user_id: int) -> str:
        user_name = self.user_service.get_user_name_by_id(user_id)
        if user_name is None:
            raise HTTPException(status_code=404, detail="User not found")

        return user_name


# Application Settings and Context

class Settings:
    def __init__(self):
        self.database_connection_string = "db://localhost"


# Application Context

class ApplicationContext(Context):
    user_controller: UserController = autowired()

    def __init__(self, settings: Settings = None):
        self.settings = settings or Settings()

    @cached_property
    def database_service(self) -> DatabaseService:
        # Since all the auto-wiring features are just shortcuts,
        # we can also instantiate the DatabaseService manually instead of using self.autowire()
        return DatabaseService(conn_str=self.settings.database_connection_string)


# Request Scoped Service

class TokenService:
    def __init__(self, db_service: DatabaseService, token: str):
        self.db_service = db_service
        self.token = token

    def is_valid(self):
        if self.token in self.db_service.load_allowed_tokens():
            return True
        return False


# Request Context

class RequestContext(Context):
    def __init__(self, parent: Context, token: str = None):
        super().__init__(parent)
        self.token = token

    @cached_property
    def token_service(self) -> TokenService:
        return self.autowire(TokenService, token=self.token)


# FastAPI Application

app = FastAPI()
ctx = ApplicationContext()


def request_context(r: Request):
    token = r.headers.get("Authorization")
    token = token.split(" ")[1] if token else None
    return RequestContext(parent=ctx, token=token)


def token_service(request_context: RequestContext = Depends(request_context)):
    return request_context.token_service


def user_controller():
    return ctx.user_controller


@app.get("/users/{user_id}")
def get_user(user_id: int,
             token_service: TokenService = Depends(token_service),
             user_controller=Depends(user_controller)
             ):
    if token_service.is_valid():
        return user_controller.get_user(user_id=int(user_id))
    else:
        return {"detail": "Invalid Token"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)

```
