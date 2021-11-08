from shapely.geometry.base import BaseGeometry

from typing_vts.shapely import X, Y, Z


class Point(BaseGeometry):
    x: X
    y: Y
    z: Z

    def __init__(self, x: X, y: Y, z: Z = None) -> None: ...

    @property
    def has_z(self) -> bool: ...
