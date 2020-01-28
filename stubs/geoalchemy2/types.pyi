from typing import Any

from sqlalchemy.types import UserDefinedType


class _GISType(UserDefinedType[Any]):
    def __init__(
            self,
            geometry_type: str = 'GEOMETRY',
            srid: int = -1,
            dimension: int = 2,
            spatial_index: bool = True,
            management: bool = False,
            use_typmod: bool = None,
            use_st_prefix: bool = True,
            ) -> None:
        ...


class Geometry(_GISType):
    ...
