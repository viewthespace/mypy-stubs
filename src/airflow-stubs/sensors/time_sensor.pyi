from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils import timezone as timezone
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class TimeSensor(BaseSensorOperator):
    target_time: Any
    def __init__(self, target_time, *args, **kwargs) -> None: ...
    def poke(self, context): ...
