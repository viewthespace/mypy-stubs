from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.file import TemporaryDirectory as TemporaryDirectory
from typing import Any

class BashSensor(BaseSensorOperator):
    template_fields: Any
    bash_command: Any
    env: Any
    output_encoding: Any
    def __init__(self, bash_command, env: Any | None = ..., output_encoding: str = ..., *args, **kwargs) -> None: ...
    sp: Any
    def poke(self, context): ...
