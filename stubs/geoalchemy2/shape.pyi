from .elements import WKBElement, WKTElement
from shapely.geometry.base import BaseGeometry
from typing import Union


def to_shape(element: Union[WKBElement, WKTElement]) -> BaseGeometry: ...


def from_shape(shape: BaseGeometry, srid: int = -1) -> WKBElement: ...
