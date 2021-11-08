from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

log: Any

class AirflowWebHDFSHookException(AirflowException): ...

class WebHDFSHook(BaseHook):
    webhdfs_conn_id: Any
    proxy_user: Any
    def __init__(self, webhdfs_conn_id: str = ..., proxy_user: Any | None = ...) -> None: ...
    def get_conn(self): ...
    def check_for_path(self, hdfs_path): ...
    def load_file(self, source, destination, overwrite: bool = ..., parallelism: int = ..., **kwargs) -> None: ...
