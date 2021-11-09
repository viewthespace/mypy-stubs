from airflow.contrib.hooks.wasb_hook import WasbHook as WasbHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class WasbDeleteBlobOperator(BaseOperator):
    template_fields: Any
    wasb_conn_id: Any
    container_name: Any
    blob_name: Any
    check_options: Any
    is_prefix: Any
    ignore_if_missing: Any
    def __init__(self, container_name, blob_name, wasb_conn_id: str = ..., check_options: Any | None = ..., is_prefix: bool = ..., ignore_if_missing: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
