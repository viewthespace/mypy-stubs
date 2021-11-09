from airflow.contrib.hooks.aws_hook import AwsHook as AwsHook
from typing import Any

class AwsLambdaHook(AwsHook):
    function_name: Any
    region_name: Any
    log_type: Any
    invocation_type: Any
    qualifier: Any
    conn: Any
    config: Any
    def __init__(self, function_name, region_name: Any | None = ..., log_type: str = ..., qualifier: str = ..., invocation_type: str = ..., config: Any | None = ..., *args, **kwargs) -> None: ...
    def get_conn(self): ...
    def invoke_lambda(self, payload): ...
