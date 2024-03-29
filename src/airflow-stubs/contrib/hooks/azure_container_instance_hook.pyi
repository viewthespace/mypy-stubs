from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class AzureContainerInstanceHook(BaseHook):
    conn_id: Any
    connection: Any
    def __init__(self, conn_id: str = ...) -> None: ...
    def get_conn(self): ...
    def create_or_update(self, resource_group, name, container_group) -> None: ...
    def get_state_exitcode_details(self, resource_group, name): ...
    def get_messages(self, resource_group, name): ...
    def get_state(self, resource_group, name): ...
    def get_logs(self, resource_group, name, tail: int = ...): ...
    def delete(self, resource_group, name) -> None: ...
    def exists(self, resource_group, name): ...
