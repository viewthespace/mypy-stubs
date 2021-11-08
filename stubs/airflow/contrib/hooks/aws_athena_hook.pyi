from airflow.contrib.hooks.aws_hook import AwsHook as AwsHook
from typing import Any

class AWSAthenaHook(AwsHook):
    INTERMEDIATE_STATES: Any
    FAILURE_STATES: Any
    SUCCESS_STATES: Any
    sleep_time: Any
    conn: Any
    def __init__(self, aws_conn_id: str = ..., sleep_time: int = ..., *args, **kwargs) -> None: ...
    def get_conn(self): ...
    def run_query(self, query, query_context, result_configuration, client_request_token: Any | None = ..., workgroup: str = ...): ...
    def check_query_status(self, query_execution_id): ...
    def get_state_change_reason(self, query_execution_id): ...
    def get_query_results(self, query_execution_id): ...
    def poll_query_status(self, query_execution_id, max_tries: Any | None = ...): ...
    def stop_query(self, query_execution_id): ...
