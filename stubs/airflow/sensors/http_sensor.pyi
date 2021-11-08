from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.http_hook import HttpHook as HttpHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class HttpSensor(BaseSensorOperator):
    template_fields: Any
    endpoint: Any
    http_conn_id: Any
    request_params: Any
    headers: Any
    extra_options: Any
    response_check: Any
    hook: Any
    def __init__(self, endpoint, http_conn_id: str = ..., method: str = ..., request_params: Any | None = ..., headers: Any | None = ..., response_check: Any | None = ..., extra_options: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
