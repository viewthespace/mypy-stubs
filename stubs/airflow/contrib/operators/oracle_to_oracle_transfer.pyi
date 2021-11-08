from airflow.hooks.oracle_hook import OracleHook as OracleHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class OracleToOracleTransfer(BaseOperator):
    template_fields: Any
    ui_color: str
    oracle_destination_conn_id: Any
    destination_table: Any
    oracle_source_conn_id: Any
    source_sql: Any
    source_sql_params: Any
    rows_chunk: Any
    def __init__(self, oracle_destination_conn_id, destination_table, oracle_source_conn_id, source_sql, source_sql_params: Any | None = ..., rows_chunk: int = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
