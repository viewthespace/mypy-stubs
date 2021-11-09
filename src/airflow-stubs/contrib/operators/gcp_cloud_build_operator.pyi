from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_cloud_build_hook import CloudBuildHook as CloudBuildHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

REGEX_REPO_PATH: Any

class BuildProcessor:
    body: Any
    def __init__(self, body) -> None: ...
    def process_body(self): ...

class CloudBuildCreateBuildOperator(BaseOperator):
    template_fields: Any
    body: Any
    project_id: Any
    gcp_conn_id: Any
    api_version: Any
    def __init__(self, body, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
