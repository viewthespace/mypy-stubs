from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook as GoogleCloudBaseHook
from typing import Any

TIME_TO_SLEEP_IN_SECONDS: int

class GcfHook(GoogleCloudBaseHook):
    api_version: Any
    def __init__(self, api_version, gcp_conn_id: str = ..., delegate_to: Any | None = ...) -> None: ...
    def get_conn(self): ...
    def get_function(self, name): ...
    def create_new_function(self, location, body, project_id: Any | None = ...) -> None: ...
    def update_function(self, name, body, update_mask) -> None: ...
    def upload_function_zip(self, location, zip_path, project_id: Any | None = ...): ...
    def delete_function(self, name) -> None: ...
