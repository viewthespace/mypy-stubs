from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook as GoogleCloudBaseHook
from typing import Any

TIME_TO_SLEEP_IN_SECONDS: int

class CloudBuildHook(GoogleCloudBaseHook):
    api_version: Any
    def __init__(self, api_version: str = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ...) -> None: ...
    def get_conn(self): ...
    def create_build(self, body, project_id: Any | None = ...): ...
