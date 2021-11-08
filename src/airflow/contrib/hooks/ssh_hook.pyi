from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class SSHHook(BaseHook):
    ssh_conn_id: Any
    remote_host: Any
    username: Any
    password: Any
    key_file: Any
    pkey: Any
    port: Any
    timeout: Any
    keepalive_interval: Any
    compress: bool
    no_host_key_check: bool
    allow_host_key_change: bool
    host_proxy: Any
    client: Any
    def __init__(self, ssh_conn_id: Any | None = ..., remote_host: Any | None = ..., username: Any | None = ..., password: Any | None = ..., key_file: Any | None = ..., port: Any | None = ..., timeout: int = ..., keepalive_interval: int = ...) -> None: ...
    def get_conn(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def get_tunnel(self, remote_port, remote_host: str = ..., local_port: Any | None = ...): ...
    def create_tunnel(self, local_port, remote_port: Any | None = ..., remote_host: str = ...): ...
