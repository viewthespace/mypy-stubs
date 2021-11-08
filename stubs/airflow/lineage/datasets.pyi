from typing import Any, List

class DataSet:
    attributes: List[str]
    type_name: str
    context: Any
    def __init__(self, qualified_name: Any | None = ..., data: Any | None = ..., **kwargs) -> None: ...
    def set_context(self, context) -> None: ...
    @property
    def qualified_name(self): ...
    def __getattr__(self, attr): ...
    def __getitem__(self, item): ...
    def __iter__(self): ...
    def as_dict(self): ...
    @staticmethod
    def map_type(name): ...

class DataBase(DataSet):
    type_name: str
    attributes: Any

class File(DataSet):
    type_name: str
    attributes: Any
    def __init__(self, name: Any | None = ..., data: Any | None = ...) -> None: ...

class HadoopFile(File):
    cluster_name: str
    attributes: Any
    type_name: str
    def __init__(self, name: Any | None = ..., data: Any | None = ...) -> None: ...

class Operator(DataSet):
    type_name: str
    attributes: Any
