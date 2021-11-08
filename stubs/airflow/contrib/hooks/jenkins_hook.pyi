from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class JenkinsHook(BaseHook):
    connection: Any
    jenkins_server: Any
    def __init__(self, conn_id: str = ...) -> None: ...
    def get_jenkins_server(self): ...
