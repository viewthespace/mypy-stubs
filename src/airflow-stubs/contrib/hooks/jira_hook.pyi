from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class JiraHook(BaseHook):
    jira_conn_id: Any
    proxies: Any
    client: Any
    def __init__(self, jira_conn_id: str = ..., proxies: Any | None = ...) -> None: ...
    def get_conn(self): ...
