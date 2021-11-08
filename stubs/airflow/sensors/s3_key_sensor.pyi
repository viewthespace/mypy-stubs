from airflow.exceptions import AirflowException as AirflowException
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class S3KeySensor(BaseSensorOperator):
    template_fields: Any
    bucket_name: Any
    bucket_key: Any
    wildcard_match: Any
    aws_conn_id: Any
    verify: Any
    def __init__(self, bucket_key, bucket_name: Any | None = ..., wildcard_match: bool = ..., aws_conn_id: str = ..., verify: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
