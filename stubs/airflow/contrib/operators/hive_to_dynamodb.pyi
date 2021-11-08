from airflow.contrib.hooks.aws_dynamodb_hook import AwsDynamoDBHook as AwsDynamoDBHook
from airflow.hooks.hive_hooks import HiveServer2Hook as HiveServer2Hook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class HiveToDynamoDBTransferOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    sql: Any
    table_name: Any
    table_keys: Any
    pre_process: Any
    pre_process_args: Any
    pre_process_kwargs: Any
    region_name: Any
    schema: Any
    hiveserver2_conn_id: Any
    aws_conn_id: Any
    def __init__(self, sql, table_name, table_keys, pre_process: Any | None = ..., pre_process_args: Any | None = ..., pre_process_kwargs: Any | None = ..., region_name: Any | None = ..., schema: str = ..., hiveserver2_conn_id: str = ..., aws_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
