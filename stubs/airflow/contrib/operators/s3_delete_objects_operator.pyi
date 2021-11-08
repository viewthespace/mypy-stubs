from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class S3DeleteObjectsOperator(BaseOperator):
    template_fields: Any
    bucket: Any
    keys: Any
    aws_conn_id: Any
    verify: Any
    def __init__(self, bucket, keys, aws_conn_id: str = ..., verify: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
