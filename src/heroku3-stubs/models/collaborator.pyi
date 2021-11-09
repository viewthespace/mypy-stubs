from . import BaseResource as BaseResource, User as User
from typing import Any

class Collaborator(BaseResource):
    app: Any
    def __init__(self) -> None: ...
    def remove(self): ...
