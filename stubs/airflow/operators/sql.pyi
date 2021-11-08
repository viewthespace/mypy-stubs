from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.models import BaseOperator as BaseOperator, SkipMixin as SkipMixin
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any, Iterable

ALLOWED_CONN_TYPE: Any

class SQLCheckOperator(BaseOperator):
    template_fields: Iterable[str]
    template_ext: Iterable[str]
    ui_color: str
    conn_id: Any
    sql: Any
    def __init__(self, sql, conn_id: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context: Any | None = ...) -> None: ...
    def get_db_hook(self): ...

class SQLValueCheckOperator(BaseOperator):
    __mapper_args__: Any
    template_fields: Iterable[str]
    template_ext: Iterable[str]
    ui_color: str
    sql: Any
    conn_id: Any
    pass_value: Any
    tol: Any
    has_tolerance: Any
    def __init__(self, sql, pass_value, tolerance: Any | None = ..., conn_id: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context: Any | None = ...) -> None: ...
    def get_db_hook(self): ...

class SQLIntervalCheckOperator(BaseOperator):
    __mapper_args__: Any
    template_fields: Iterable[str]
    template_ext: Iterable[str]
    ui_color: str
    ratio_formulas: Any
    ratio_formula: Any
    ignore_zero: Any
    table: Any
    metrics_thresholds: Any
    metrics_sorted: Any
    date_filter_column: Any
    days_back: Any
    conn_id: Any
    sql1: Any
    sql2: Any
    def __init__(self, table, metrics_thresholds, date_filter_column: str = ..., days_back: int = ..., ratio_formula: str = ..., ignore_zero: bool = ..., conn_id: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context: Any | None = ...) -> None: ...
    def get_db_hook(self): ...

class SQLThresholdCheckOperator(BaseOperator):
    template_fields: Iterable[str]
    template_ext: Iterable[str]
    sql: Any
    conn_id: Any
    min_threshold: Any
    max_threshold: Any
    def __init__(self, sql, min_threshold, max_threshold, conn_id: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context: Any | None = ...) -> None: ...
    def push(self, meta_data) -> None: ...
    def get_db_hook(self): ...

class BranchSQLOperator(BaseOperator, SkipMixin):
    template_fields: Any
    template_ext: Any
    ui_color: str
    ui_fgcolor: str
    conn_id: Any
    sql: Any
    parameters: Any
    follow_task_ids_if_true: Any
    follow_task_ids_if_false: Any
    database: Any
    def __init__(self, sql, follow_task_ids_if_true, follow_task_ids_if_false, conn_id: str = ..., database: Any | None = ..., parameters: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
