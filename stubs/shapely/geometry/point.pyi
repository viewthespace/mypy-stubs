from typing import NewType

from shapely.geometry.base import BaseGeometry

X = NewType('X', float)
Y = NewType('Y', float)
Z = NewType('Z', float)


class Point(BaseGeometry):
    x: X
    y: Y
    z: Z

    def __init__(self, x: X, y: Y, z: Z = None) -> None: ...

    @property
    def has_z(self) -> bool: ...
