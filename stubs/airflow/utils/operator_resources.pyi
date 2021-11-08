from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from typing import Any

MB: int
GB: Any
TB: Any
PB: Any
EB: Any

class Resource:
    def __init__(self, name, units_str, qty) -> None: ...
    def __eq__(self, other): ...
    @property
    def name(self): ...
    @property
    def units_str(self): ...
    @property
    def qty(self): ...

class CpuResource(Resource):
    def __init__(self, qty) -> None: ...

class RamResource(Resource):
    def __init__(self, qty) -> None: ...

class DiskResource(Resource):
    def __init__(self, qty) -> None: ...

class GpuResource(Resource):
    def __init__(self, qty) -> None: ...

class Resources:
    cpus: Any
    ram: Any
    disk: Any
    gpus: Any
    def __init__(self, cpus=..., ram=..., disk=..., gpus=...) -> None: ...
    def __eq__(self, other): ...
