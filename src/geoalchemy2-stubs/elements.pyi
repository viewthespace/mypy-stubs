from typing import Any

from sqlalchemy.sql import functions


class _SpatialElement(functions.Function[Any]):
    @property
    def desc(self) -> str: pass


class WKBElement(_SpatialElement):
    ...


class WKTElement(_SpatialElement):
    ...
