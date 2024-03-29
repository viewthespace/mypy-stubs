from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.druid_hook import DruidDbApiHook as DruidDbApiHook
from airflow.operators.check_operator import CheckOperator as CheckOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class DruidCheckOperator(CheckOperator):
    druid_broker_conn_id: Any
    sql: Any
    def __init__(self, sql, druid_broker_conn_id: str = ..., *args, **kwargs) -> None: ...
    def get_db_hook(self): ...
    def get_first(self, sql): ...
    def execute(self, context: Any | None = ...) -> None: ...
