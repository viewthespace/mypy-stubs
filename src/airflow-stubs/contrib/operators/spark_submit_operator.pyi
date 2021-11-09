from airflow.contrib.hooks.spark_submit_hook import SparkSubmitHook as SparkSubmitHook
from airflow.models import BaseOperator as BaseOperator
from airflow.settings import WEB_COLORS as WEB_COLORS
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SparkSubmitOperator(BaseOperator):
    template_fields: Any
    ui_color: Any
    def __init__(self, application: str = ..., conf: Any | None = ..., conn_id: str = ..., files: Any | None = ..., py_files: Any | None = ..., archives: Any | None = ..., driver_class_path: Any | None = ..., jars: Any | None = ..., java_class: Any | None = ..., packages: Any | None = ..., exclude_packages: Any | None = ..., repositories: Any | None = ..., total_executor_cores: Any | None = ..., executor_cores: Any | None = ..., executor_memory: Any | None = ..., driver_memory: Any | None = ..., keytab: Any | None = ..., principal: Any | None = ..., proxy_user: Any | None = ..., name: str = ..., num_executors: Any | None = ..., status_poll_interval: int = ..., application_args: Any | None = ..., env_vars: Any | None = ..., verbose: bool = ..., spark_binary: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
    def on_kill(self) -> None: ...
