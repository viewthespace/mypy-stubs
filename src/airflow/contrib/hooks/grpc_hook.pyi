from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class GrpcHook(BaseHook):
    grpc_conn_id: Any
    conn: Any
    extras: Any
    interceptors: Any
    custom_connection_func: Any
    def __init__(self, grpc_conn_id, interceptors: Any | None = ..., custom_connection_func: Any | None = ...) -> None: ...
    def get_conn(self): ...
    def run(self, stub_class, call_func, streaming: bool = ..., data: Any | None = ...) -> None: ...
