from airflow.contrib.hooks.datadog_hook import DatadogHook as DatadogHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils import apply_defaults as apply_defaults
from typing import Any

class DatadogSensor(BaseSensorOperator):
    ui_color: str
    datadog_conn_id: Any
    from_seconds_ago: Any
    up_to_seconds_from_now: Any
    priority: Any
    sources: Any
    tags: Any
    response_check: Any
    def __init__(self, datadog_conn_id: str = ..., from_seconds_ago: int = ..., up_to_seconds_from_now: int = ..., priority: Any | None = ..., sources: Any | None = ..., tags: Any | None = ..., response_check: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
