from pprint import pprint as pprint
from typing import Any
from urllib.parse import quote as quote

class BaseResource:
    order_by: str
    def __init__(self) -> None: ...
    def dict(self): ...
    def change_connection(self, h): ...
    @classmethod
    def new_from_dict(cls, d, h: Any | None = ..., **kwargs): ...

class Price(BaseResource):
    app: Any
    def __init__(self) -> None: ...

class Plan(BaseResource): ...

class Stack(BaseResource):
    app: Any
    def __init__(self) -> None: ...

class User(BaseResource):
    app: Any
    def __init__(self) -> None: ...

class Organization(BaseResource):
    app: Any
    def __init__(self) -> None: ...

class RateLimit(BaseResource):
    app: Any
    def __init__(self) -> None: ...
