from . import BaseResource as BaseResource, User as User
from .slug import Slug as Slug
from typing import Any

class Release(BaseResource):
    order_by: str
    app: Any
    def __init__(self) -> None: ...
