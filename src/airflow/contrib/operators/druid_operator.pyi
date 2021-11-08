from airflow.hooks.druid_hook import DruidHook as DruidHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class DruidOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    conn_id: Any
    max_ingestion_time: Any
    index_spec_str: Any
    def __init__(self, json_index_file, druid_ingest_conn_id: str = ..., max_ingestion_time: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
