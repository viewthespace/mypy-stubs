from airflow.hooks.oracle_hook import OracleHook as OracleHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class OracleOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    oracle_conn_id: Any
    sql: Any
    autocommit: Any
    parameters: Any
    def __init__(self, sql, oracle_conn_id: str = ..., parameters: Any | None = ..., autocommit: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
