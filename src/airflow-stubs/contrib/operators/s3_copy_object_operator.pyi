from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class S3CopyObjectOperator(BaseOperator):
    template_fields: Any
    source_bucket_key: Any
    dest_bucket_key: Any
    source_bucket_name: Any
    dest_bucket_name: Any
    source_version_id: Any
    aws_conn_id: Any
    verify: Any
    def __init__(self, source_bucket_key, dest_bucket_key, source_bucket_name: Any | None = ..., dest_bucket_name: Any | None = ..., source_version_id: Any | None = ..., aws_conn_id: str = ..., verify: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
