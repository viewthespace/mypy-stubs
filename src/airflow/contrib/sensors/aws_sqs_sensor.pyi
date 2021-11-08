from airflow.contrib.hooks.aws_sqs_hook import SQSHook as SQSHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SQSSensor(BaseSensorOperator):
    template_fields: Any
    sqs_queue: Any
    aws_conn_id: Any
    max_messages: Any
    wait_time_seconds: Any
    def __init__(self, sqs_queue, aws_conn_id: str = ..., max_messages: int = ..., wait_time_seconds: int = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
