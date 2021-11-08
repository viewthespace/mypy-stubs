from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook as GoogleCloudBaseHook
from typing import Any

class GoogleDriveHook(GoogleCloudBaseHook):
    api_version: Any
    def __init__(self, api_version: str = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ...) -> None: ...
    def get_conn(self): ...
    def upload_file(self, local_location, remote_location): ...
