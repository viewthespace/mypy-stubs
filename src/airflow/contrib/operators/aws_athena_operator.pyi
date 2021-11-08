from airflow.contrib.hooks.aws_athena_hook import AWSAthenaHook as AWSAthenaHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class AWSAthenaOperator(BaseOperator):
    ui_color: str
    template_fields: Any
    template_ext: Any
    query: Any
    database: Any
    output_location: Any
    aws_conn_id: Any
    client_request_token: Any
    workgroup: Any
    query_execution_context: Any
    result_configuration: Any
    sleep_time: Any
    max_tries: Any
    query_execution_id: Any
    hook: Any
    def __init__(self, query, database, output_location, aws_conn_id: str = ..., client_request_token: Any | None = ..., query_execution_context: Any | None = ..., result_configuration: Any | None = ..., sleep_time: int = ..., max_tries: Any | None = ..., workgroup: str = ..., *args, **kwargs) -> None: ...
    def get_hook(self): ...
    def execute(self, context): ...
    def on_kill(self) -> None: ...
