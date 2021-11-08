from airflow.contrib.hooks.aws_hook import AwsHook as AwsHook
from typing import Any

class AwsFirehoseHook(AwsHook):
    delivery_stream: Any
    region_name: Any
    conn: Any
    def __init__(self, delivery_stream, region_name: Any | None = ..., *args, **kwargs) -> None: ...
    def get_conn(self): ...
    def put_records(self, records): ...
