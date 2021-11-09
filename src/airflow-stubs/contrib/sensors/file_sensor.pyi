from airflow.contrib.hooks.fs_hook import FSHook as FSHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class FileSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    filepath: Any
    fs_conn_id: Any
    def __init__(self, filepath, fs_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
