from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class WebHdfsSensor(BaseSensorOperator):
    template_fields: Any
    filepath: Any
    webhdfs_conn_id: Any
    def __init__(self, filepath, webhdfs_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
