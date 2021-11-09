from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GenericTransfer(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    sql: Any
    destination_table: Any
    source_conn_id: Any
    destination_conn_id: Any
    preoperator: Any
    def __init__(self, sql, destination_table, source_conn_id, destination_conn_id, preoperator: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
