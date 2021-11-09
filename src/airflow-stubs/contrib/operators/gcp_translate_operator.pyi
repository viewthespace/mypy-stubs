from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_translate_hook import CloudTranslateHook as CloudTranslateHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class CloudTranslateTextOperator(BaseOperator):
    template_fields: Any
    values: Any
    target_language: Any
    format_: Any
    source_language: Any
    model: Any
    gcp_conn_id: Any
    def __init__(self, values, target_language, format_, source_language, model, gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
