from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook as GoogleCloudBaseHook
from typing import Any

class CloudTranslateHook(GoogleCloudBaseHook):
    def __init__(self, gcp_conn_id: str = ...) -> None: ...
    def get_conn(self): ...
    def translate(self, values, target_language, format_: Any | None = ..., source_language: Any | None = ..., model: Any | None = ...): ...