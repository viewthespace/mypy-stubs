from airflow.contrib.hooks.spark_sql_hook import SparkSqlHook as SparkSqlHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SparkSqlOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    def __init__(self, sql, conf: Any | None = ..., conn_id: str = ..., total_executor_cores: Any | None = ..., executor_cores: Any | None = ..., executor_memory: Any | None = ..., keytab: Any | None = ..., principal: Any | None = ..., master: str = ..., name: str = ..., num_executors: Any | None = ..., verbose: bool = ..., yarn_queue: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
    def on_kill(self) -> None: ...
