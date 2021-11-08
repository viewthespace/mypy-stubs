from airflow.contrib.hooks.databricks_hook import DatabricksHook as DatabricksHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

XCOM_RUN_ID_KEY: str
XCOM_RUN_PAGE_URL_KEY: str

class DatabricksSubmitRunOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    ui_fgcolor: str
    json: Any
    databricks_conn_id: Any
    polling_period_seconds: Any
    databricks_retry_limit: Any
    databricks_retry_delay: Any
    run_id: Any
    do_xcom_push: Any
    def __init__(self, json: Any | None = ..., spark_jar_task: Any | None = ..., notebook_task: Any | None = ..., new_cluster: Any | None = ..., existing_cluster_id: Any | None = ..., libraries: Any | None = ..., run_name: Any | None = ..., timeout_seconds: Any | None = ..., databricks_conn_id: str = ..., polling_period_seconds: int = ..., databricks_retry_limit: int = ..., databricks_retry_delay: int = ..., do_xcom_push: bool = ..., **kwargs) -> None: ...
    def get_hook(self): ...
    def execute(self, context) -> None: ...
    def on_kill(self) -> None: ...

class DatabricksRunNowOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    ui_fgcolor: str
    json: Any
    databricks_conn_id: Any
    polling_period_seconds: Any
    databricks_retry_limit: Any
    databricks_retry_delay: Any
    run_id: Any
    do_xcom_push: Any
    def __init__(self, job_id, json: Any | None = ..., notebook_params: Any | None = ..., python_params: Any | None = ..., spark_submit_params: Any | None = ..., databricks_conn_id: str = ..., polling_period_seconds: int = ..., databricks_retry_limit: int = ..., databricks_retry_delay: int = ..., do_xcom_push: bool = ..., **kwargs) -> None: ...
    def get_hook(self): ...
    def execute(self, context) -> None: ...
    def on_kill(self) -> None: ...
