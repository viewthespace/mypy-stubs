from airflow.contrib.hooks.wasb_hook import WasbHook as WasbHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class FileToWasbOperator(BaseOperator):
    template_fields: Any
    file_path: Any
    container_name: Any
    blob_name: Any
    wasb_conn_id: Any
    load_options: Any
    def __init__(self, file_path, container_name, blob_name, wasb_conn_id: str = ..., load_options: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
