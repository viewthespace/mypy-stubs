from airflow.hooks.presto_hook import PrestoHook as PrestoHook
from airflow.operators.check_operator import CheckOperator as CheckOperator, IntervalCheckOperator as IntervalCheckOperator, ValueCheckOperator as ValueCheckOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class PrestoCheckOperator(CheckOperator):
    presto_conn_id: Any
    sql: Any
    def __init__(self, sql, presto_conn_id: str = ..., *args, **kwargs) -> None: ...
    def get_db_hook(self): ...

class PrestoValueCheckOperator(ValueCheckOperator):
    presto_conn_id: Any
    def __init__(self, sql, pass_value, tolerance: Any | None = ..., presto_conn_id: str = ..., *args, **kwargs) -> None: ...
    def get_db_hook(self): ...

class PrestoIntervalCheckOperator(IntervalCheckOperator):
    presto_conn_id: Any
    def __init__(self, table, metrics_thresholds, date_filter_column: str = ..., days_back: int = ..., presto_conn_id: str = ..., *args, **kwargs) -> None: ...
    def get_db_hook(self): ...
