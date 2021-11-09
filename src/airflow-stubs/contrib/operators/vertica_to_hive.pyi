from airflow.contrib.hooks.vertica_hook import VerticaHook as VerticaHook
from airflow.hooks.hive_hooks import HiveCliHook as HiveCliHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class VerticaToHiveTransfer(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    sql: Any
    hive_table: Any
    partition: Any
    create: Any
    recreate: Any
    delimiter: Any
    vertica_conn_id: Any
    hive_cli_conn_id: Any
    def __init__(self, sql, hive_table, create: bool = ..., recreate: bool = ..., partition: Any | None = ..., delimiter=..., vertica_conn_id: str = ..., hive_cli_conn_id: str = ..., *args, **kwargs) -> None: ...
    @classmethod
    def type_map(cls, vertica_type): ...
    def execute(self, context) -> None: ...
