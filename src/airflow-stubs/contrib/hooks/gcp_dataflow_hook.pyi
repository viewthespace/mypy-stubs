from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook as GoogleCloudBaseHook
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

DEFAULT_DATAFLOW_LOCATION: str

class _DataflowJob(LoggingMixin):
    def __init__(self, dataflow, project_number, name, location, poll_sleep: int = ..., job_id: Any | None = ..., num_retries: Any | None = ...) -> None: ...
    def wait_for_done(self): ...
    def get(self): ...

class _Dataflow(LoggingMixin):
    def __init__(self, cmd) -> None: ...
    def wait_for_done(self): ...

class DataFlowHook(GoogleCloudBaseHook):
    poll_sleep: Any
    def __init__(self, gcp_conn_id: str = ..., delegate_to: Any | None = ..., poll_sleep: int = ...) -> None: ...
    def get_conn(self): ...
    def start_java_dataflow(self, job_name, variables, dataflow, job_class: Any | None = ..., append_job_name: bool = ...): ...
    def start_template_dataflow(self, job_name, variables, parameters, dataflow_template, append_job_name: bool = ...) -> None: ...
    def start_python_dataflow(self, job_name, variables, dataflow, py_options, append_job_name: bool = ...): ...
