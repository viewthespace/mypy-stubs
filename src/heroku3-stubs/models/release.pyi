from . import BaseResource as BaseResource, User as User
from .slug import Slug as Slug
import datetime as dt
from typing import Any

class Release(BaseResource):
    order_by: str
    app: Any
    description: str
    updated_at: dt.datetime
    id: str
    status: str

    def __init__(self) -> None: ...
