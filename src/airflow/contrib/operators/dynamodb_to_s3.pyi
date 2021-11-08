from airflow.contrib.hooks.aws_dynamodb_hook import AwsDynamoDBHook as AwsDynamoDBHook
from airflow.hooks.S3_hook import S3Hook as S3Hook
from airflow.models.baseoperator import BaseOperator as BaseOperator
from typing import Any, Callable, Dict, Optional

class DynamoDBToS3Operator(BaseOperator):
    file_size: Any
    process_func: Any
    dynamodb_table_name: Any
    dynamodb_scan_kwargs: Any
    s3_bucket_name: Any
    s3_key_prefix: Any
    def __init__(self, dynamodb_table_name: str, s3_bucket_name: str, file_size, dynamodb_scan_kwargs: Optional[Dict[str, Any]] = ..., s3_key_prefix: str = ..., process_func: Callable[[Dict[str, Any]], bytes] = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
