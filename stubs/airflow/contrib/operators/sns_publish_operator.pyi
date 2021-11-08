from airflow.contrib.hooks.aws_sns_hook import AwsSnsHook as AwsSnsHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SnsPublishOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    target_arn: Any
    message: Any
    subject: Any
    message_attributes: Any
    aws_conn_id: Any
    def __init__(self, target_arn, message, aws_conn_id: str = ..., subject: Any | None = ..., message_attributes: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
