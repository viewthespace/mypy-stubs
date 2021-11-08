from typing import Any
from wtforms.validators import EqualTo

class GreaterEqualThan(EqualTo):
    def __call__(self, form, field) -> None: ...

class ValidJson:
    message: Any
    def __init__(self, message: Any | None = ...) -> None: ...
    def __call__(self, form, field) -> None: ...
