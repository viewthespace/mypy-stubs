from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

class DockerHook(BaseHook, LoggingMixin):
    def __init__(self, docker_conn_id: str = ..., base_url: Any | None = ..., version: Any | None = ..., tls: Any | None = ...) -> None: ...
    def get_conn(self): ...
