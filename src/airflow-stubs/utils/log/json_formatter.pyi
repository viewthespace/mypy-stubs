import logging
from typing import Any

def merge_dicts(dict1, dict2): ...

class JSONFormatter(logging.Formatter):
    json_fields: Any
    extras: Any
    def __init__(self, fmt: Any | None = ..., datefmt: Any | None = ..., json_fields: Any | None = ..., extras: Any | None = ...) -> None: ...
    def format(self, record): ...
