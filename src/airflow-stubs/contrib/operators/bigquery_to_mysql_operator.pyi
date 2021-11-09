from airflow.contrib.hooks.bigquery_hook import BigQueryHook as BigQueryHook
from airflow.hooks.mysql_hook import MySqlHook as MySqlHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class BigQueryToMySqlOperator(BaseOperator):
    template_fields: Any
    selected_fields: Any
    gcp_conn_id: Any
    mysql_conn_id: Any
    database: Any
    mysql_table: Any
    replace: Any
    delegate_to: Any
    batch_size: Any
    def __init__(self, dataset_table, mysql_table, selected_fields: Any | None = ..., gcp_conn_id: str = ..., mysql_conn_id: str = ..., database: Any | None = ..., delegate_to: Any | None = ..., replace: bool = ..., batch_size: int = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
