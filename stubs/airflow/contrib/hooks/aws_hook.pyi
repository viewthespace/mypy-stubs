from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class AwsHook(BaseHook):
    aws_conn_id: Any
    verify: Any
    def __init__(self, aws_conn_id: str = ..., verify: Any | None = ...) -> None: ...
    def get_client_type(self, client_type, region_name: Any | None = ..., config: Any | None = ...): ...
    def get_resource_type(self, resource_type, region_name: Any | None = ..., config: Any | None = ...): ...
    def get_session(self, region_name: Any | None = ...): ...
    def get_credentials(self, region_name: Any | None = ...): ...
    def expand_role(self, role): ...
