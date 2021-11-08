from airflow.exceptions import AirflowException as AirflowException
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils import apply_defaults as apply_defaults
from typing import Any

class EmrBaseSensor(BaseSensorOperator):
    ui_color: str
    aws_conn_id: Any
    def __init__(self, aws_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
