from airflow.contrib.hooks.gcp_dataflow_hook import DataFlowHook as DataFlowHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.version import version as version
from typing import Any

class DataFlowJavaOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    gcp_conn_id: Any
    delegate_to: Any
    jar: Any
    job_name: Any
    dataflow_default_options: Any
    options: Any
    poll_sleep: Any
    job_class: Any
    def __init__(self, jar, job_name: str = ..., dataflow_default_options: Any | None = ..., options: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., poll_sleep: int = ..., job_class: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class DataflowTemplateOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    gcp_conn_id: Any
    delegate_to: Any
    dataflow_default_options: Any
    poll_sleep: Any
    template: Any
    job_name: Any
    parameters: Any
    def __init__(self, template, job_name: str = ..., dataflow_default_options: Any | None = ..., parameters: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., poll_sleep: int = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class DataFlowPythonOperator(BaseOperator):
    template_fields: Any
    py_file: Any
    job_name: Any
    py_options: Any
    dataflow_default_options: Any
    options: Any
    gcp_conn_id: Any
    delegate_to: Any
    poll_sleep: Any
    def __init__(self, py_file, job_name: str = ..., py_options: Any | None = ..., dataflow_default_options: Any | None = ..., options: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., poll_sleep: int = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class GoogleCloudBucketHelper:
    GCS_PREFIX_LENGTH: int
    def __init__(self, gcp_conn_id: str = ..., delegate_to: Any | None = ...) -> None: ...
    def google_cloud_to_local(self, file_name): ...
