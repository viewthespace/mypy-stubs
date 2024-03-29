from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.kubernetes import kube_client as kube_client
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

class SparkSubmitHook(BaseHook, LoggingMixin):
    def __init__(self, conf: Any | None = ..., conn_id: str = ..., files: Any | None = ..., py_files: Any | None = ..., archives: Any | None = ..., driver_class_path: Any | None = ..., jars: Any | None = ..., java_class: Any | None = ..., packages: Any | None = ..., exclude_packages: Any | None = ..., repositories: Any | None = ..., total_executor_cores: Any | None = ..., executor_cores: Any | None = ..., executor_memory: Any | None = ..., driver_memory: Any | None = ..., keytab: Any | None = ..., principal: Any | None = ..., proxy_user: Any | None = ..., name: str = ..., num_executors: Any | None = ..., status_poll_interval: int = ..., application_args: Any | None = ..., env_vars: Any | None = ..., verbose: bool = ..., spark_binary: Any | None = ...) -> None: ...
    def get_conn(self) -> None: ...
    def submit(self, application: str = ..., **kwargs) -> None: ...
    def on_kill(self) -> None: ...
