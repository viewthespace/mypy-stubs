from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class S3FileTransformOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    source_s3_key: Any
    source_aws_conn_id: Any
    source_verify: Any
    dest_s3_key: Any
    dest_aws_conn_id: Any
    dest_verify: Any
    replace: Any
    transform_script: Any
    select_expression: Any
    output_encoding: Any
    def __init__(self, source_s3_key, dest_s3_key, transform_script: Any | None = ..., select_expression: Any | None = ..., source_aws_conn_id: str = ..., source_verify: Any | None = ..., dest_aws_conn_id: str = ..., dest_verify: Any | None = ..., replace: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
