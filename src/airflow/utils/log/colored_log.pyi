from colorlog import TTYColoredFormatter
from typing import Any

DEFAULT_COLORS: Any
BOLD_ON: Any
BOLD_OFF: Any

class CustomTTYColoredFormatter(TTYColoredFormatter):
    def __init__(self, *args, **kwargs) -> None: ...
    def format(self, record): ...
