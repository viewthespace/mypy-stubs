from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class S3PrefixSensor(BaseSensorOperator):
    template_fields: Any
    bucket_name: Any
    prefix: Any
    delimiter: Any
    full_url: Any
    aws_conn_id: Any
    verify: Any
    def __init__(self, bucket_name, prefix, delimiter: str = ..., aws_conn_id: str = ..., verify: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
