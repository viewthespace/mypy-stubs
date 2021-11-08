from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

snakebite_loaded: bool

class HDFSHookException(AirflowException): ...

class HDFSHook(BaseHook):
    hdfs_conn_id: Any
    proxy_user: Any
    autoconfig: Any
    def __init__(self, hdfs_conn_id: str = ..., proxy_user: Any | None = ..., autoconfig: bool = ...) -> None: ...
    def get_conn(self): ...
