from . import BaseResource as BaseResource
from typing import Any

class Formation(BaseResource):
    app: Any
    def __init__(self) -> None: ...
    def scale(self, quantity): ...
    def resize(self, size): ...
    def update(self, size: Any | None = ..., quantity: Any | None = ...): ...
