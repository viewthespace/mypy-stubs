from airflow.contrib.hooks.bigquery_hook import BigQueryHook as BigQueryHook
from airflow.operators.sql import SQLCheckOperator as SQLCheckOperator, SQLIntervalCheckOperator as SQLIntervalCheckOperator, SQLValueCheckOperator as SQLValueCheckOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class BigQueryCheckOperator(SQLCheckOperator):
    template_fields: Any
    template_ext: Any
    bigquery_conn_id: Any
    sql: Any
    use_legacy_sql: Any
    def __init__(self, sql, bigquery_conn_id: str = ..., use_legacy_sql: bool = ..., *args, **kwargs) -> None: ...
    def get_db_hook(self): ...

class BigQueryValueCheckOperator(SQLValueCheckOperator):
    template_fields: Any
    template_ext: Any
    bigquery_conn_id: Any
    use_legacy_sql: Any
    def __init__(self, sql, pass_value, tolerance: Any | None = ..., bigquery_conn_id: str = ..., use_legacy_sql: bool = ..., *args, **kwargs) -> None: ...
    def get_db_hook(self): ...

class BigQueryIntervalCheckOperator(SQLIntervalCheckOperator):
    template_fields: Any
    bigquery_conn_id: Any
    use_legacy_sql: Any
    def __init__(self, table, metrics_thresholds, date_filter_column: str = ..., days_back: int = ..., bigquery_conn_id: str = ..., use_legacy_sql: bool = ..., *args, **kwargs) -> None: ...
    def get_db_hook(self): ...
