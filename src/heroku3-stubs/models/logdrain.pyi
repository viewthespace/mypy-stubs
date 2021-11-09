from . import BaseResource as BaseResource
from .addon import Addon as Addon
from typing import Any

class LogDrain(BaseResource):
    app: Any
    def __init__(self) -> None: ...
    def remove(self): ...
