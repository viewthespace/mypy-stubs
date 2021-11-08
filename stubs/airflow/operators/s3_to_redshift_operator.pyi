from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.hooks.postgres_hook import PostgresHook as PostgresHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class S3ToRedshiftTransfer(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    schema: Any
    table: Any
    s3_bucket: Any
    s3_key: Any
    redshift_conn_id: Any
    aws_conn_id: Any
    verify: Any
    copy_options: Any
    autocommit: Any
    parameters: Any
    def __init__(self, schema, table, s3_bucket, s3_key, redshift_conn_id: str = ..., aws_conn_id: str = ..., verify: Any | None = ..., copy_options=..., autocommit: bool = ..., parameters: Any | None = ..., *args, **kwargs) -> None: ...
    hook: Any
    s3: Any
    def execute(self, context) -> None: ...
