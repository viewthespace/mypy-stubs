from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class WasbHook(BaseHook):
    conn_id: Any
    connection: Any
    def __init__(self, wasb_conn_id: str = ...) -> None: ...
    def get_conn(self): ...
    def check_for_blob(self, container_name, blob_name, **kwargs): ...
    def check_for_prefix(self, container_name, prefix, **kwargs): ...
    def load_file(self, file_path, container_name, blob_name, **kwargs) -> None: ...
    def load_string(self, string_data, container_name, blob_name, **kwargs) -> None: ...
    def get_file(self, file_path, container_name, blob_name, **kwargs): ...
    def read_file(self, container_name, blob_name, **kwargs): ...
    def delete_file(self, container_name, blob_name, is_prefix: bool = ..., ignore_if_missing: bool = ..., **kwargs) -> None: ...
