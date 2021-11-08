from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.hooks.hive_hooks import HiveCliHook as HiveCliHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.compression import uncompress_file as uncompress_file
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.file import TemporaryDirectory as TemporaryDirectory
from typing import Any

class S3ToHiveTransfer(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    s3_key: Any
    field_dict: Any
    hive_table: Any
    delimiter: Any
    create: Any
    recreate: Any
    partition: Any
    headers: Any
    check_headers: Any
    wildcard_match: Any
    hive_cli_conn_id: Any
    aws_conn_id: Any
    verify: Any
    input_compressed: Any
    tblproperties: Any
    select_expression: Any
    def __init__(self, s3_key, field_dict, hive_table, delimiter: str = ..., create: bool = ..., recreate: bool = ..., partition: Any | None = ..., headers: bool = ..., check_headers: bool = ..., wildcard_match: bool = ..., aws_conn_id: str = ..., verify: Any | None = ..., hive_cli_conn_id: str = ..., input_compressed: bool = ..., tblproperties: Any | None = ..., select_expression: Any | None = ..., *args, **kwargs) -> None: ...
    s3: Any
    hive: Any
    def execute(self, context) -> None: ...
