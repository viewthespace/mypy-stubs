from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.hive_hooks import HiveMetastoreHook as HiveMetastoreHook
from airflow.hooks.mysql_hook import MySqlHook as MySqlHook
from airflow.hooks.presto_hook import PrestoHook as PrestoHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class HiveStatsCollectionOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    table: Any
    partition: Any
    extra_exprs: Any
    excluded_columns: Any
    metastore_conn_id: Any
    presto_conn_id: Any
    mysql_conn_id: Any
    assignment_func: Any
    ds: str
    dttm: str
    def __init__(self, table, partition, extra_exprs: Any | None = ..., excluded_columns: Any | None = ..., assignment_func: Any | None = ..., metastore_conn_id: str = ..., presto_conn_id: str = ..., mysql_conn_id: str = ..., *args, **kwargs) -> None: ...
    def get_default_exprs(self, col, col_type): ...
    def execute(self, context: Any | None = ...) -> None: ...
