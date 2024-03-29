from . import BaseResource as BaseResource, User as User
from typing import Any

class Grant(BaseResource):
    def __init__(self) -> None: ...

class RefreshToken(BaseResource):
    def __init__(self) -> None: ...

class AccessToken(BaseResource):
    def __init__(self) -> None: ...

class OAuthClient(BaseResource):
    def __init__(self) -> None: ...
    def delete(self): ...
    def update(self, name: Any | None = ..., redirect_uri: Any | None = ...): ...

class OAuthAuthorization(BaseResource):
    order_by: str
    def __init__(self) -> None: ...
    def delete(self): ...

class OAuthToken(BaseResource):
    order_by: str
    def __init__(self) -> None: ...

class Session(BaseResource):
    order_by: str
    def __init__(self) -> None: ...
