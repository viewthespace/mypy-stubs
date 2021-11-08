from airflow.contrib.hooks.aws_sqs_hook import SQSHook as SQSHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SQSPublishOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    sqs_queue: Any
    aws_conn_id: Any
    message_content: Any
    delay_seconds: Any
    message_attributes: Any
    def __init__(self, sqs_queue, message_content, message_attributes: Any | None = ..., delay_seconds: int = ..., aws_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
