from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from builtins import str
from typing import Any, Iterable

class SqlSensor(BaseSensorOperator):
    template_fields: Iterable[str]
    template_ext: Iterable[str]
    ui_color: str
    conn_id: Any
    sql: Any
    parameters: Any
    success: Any
    failure: Any
    fail_on_empty: Any
    allow_null: Any
    def __init__(self, conn_id, sql, parameters: Any | None = ..., success: Any | None = ..., failure: Any | None = ..., fail_on_empty: bool = ..., allow_null: bool = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
