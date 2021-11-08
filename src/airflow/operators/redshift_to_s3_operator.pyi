from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.hooks.postgres_hook import PostgresHook as PostgresHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class RedshiftToS3Transfer(BaseOperator):
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
    unload_options: Any
    autocommit: Any
    include_header: Any
    table_as_file_name: Any
    def __init__(self, schema, table, s3_bucket, s3_key, redshift_conn_id: str = ..., aws_conn_id: str = ..., verify: Any | None = ..., unload_options=..., autocommit: bool = ..., include_header: bool = ..., table_as_file_name: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
