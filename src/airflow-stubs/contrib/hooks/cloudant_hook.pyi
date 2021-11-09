from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

log: Any

class CloudantHook(BaseHook):
    cloudant_conn_id: Any
    def __init__(self, cloudant_conn_id: str = ...) -> None: ...
    def get_conn(self): ...
    def db(self): ...
