from . import BaseResource as BaseResource
from typing import Any

class Domain(BaseResource):
    order_by: str
    app: Any
    def __init__(self) -> None: ...
    def remove(self): ...
