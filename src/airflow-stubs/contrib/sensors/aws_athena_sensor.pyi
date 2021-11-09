from airflow.contrib.hooks.aws_athena_hook import AWSAthenaHook as AWSAthenaHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class AthenaSensor(BaseSensorOperator):
    INTERMEDIATE_STATES: Any
    FAILURE_STATES: Any
    SUCCESS_STATES: Any
    template_fields: Any
    template_ext: Any
    ui_color: str
    aws_conn_id: Any
    query_execution_id: Any
    hook: Any
    sleep_time: Any
    max_retires: Any
    def __init__(self, query_execution_id, max_retires: Any | None = ..., aws_conn_id: str = ..., sleep_time: int = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
    def get_hook(self): ...
