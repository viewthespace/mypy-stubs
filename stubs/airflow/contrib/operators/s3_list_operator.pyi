from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any, Iterable

class S3ListOperator(BaseOperator):
    template_fields: Iterable[str]
    ui_color: str
    bucket: Any
    prefix: Any
    delimiter: Any
    aws_conn_id: Any
    verify: Any
    def __init__(self, bucket, prefix: str = ..., delimiter: str = ..., aws_conn_id: str = ..., verify: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
