from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class AzureContainerRegistryHook(BaseHook):
    conn_id: Any
    connection: Any
    def __init__(self, conn_id: str = ...) -> None: ...
    def get_conn(self): ...
