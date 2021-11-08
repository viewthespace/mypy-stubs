from airflow.contrib.hooks.aws_hook import AwsHook as AwsHook
from airflow.exceptions import AirflowException as AirflowException
from typing import Any

class AwsDynamoDBHook(AwsHook):
    table_keys: Any
    table_name: Any
    region_name: Any
    conn: Any
    def __init__(self, table_keys: Any | None = ..., table_name: Any | None = ..., region_name: Any | None = ..., *args, **kwargs) -> None: ...
    def get_conn(self): ...
    def write_batch_data(self, items): ...
