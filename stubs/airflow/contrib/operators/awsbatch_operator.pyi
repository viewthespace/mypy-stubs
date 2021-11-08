from airflow.contrib.hooks.aws_hook import AwsHook as AwsHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils import apply_defaults as apply_defaults
from typing import Any

class AWSBatchOperator(BaseOperator):
    MAX_RETRIES: int
    STATUS_RETRIES: int
    ui_color: str
    client: Any
    arn: Any
    template_fields: Any
    job_name: Any
    aws_conn_id: Any
    region_name: Any
    job_definition: Any
    job_queue: Any
    overrides: Any
    array_properties: Any
    parameters: Any
    max_retries: Any
    status_retries: Any
    jobId: Any
    jobName: Any
    hook: Any
    def __init__(self, job_name, job_definition, job_queue, overrides, array_properties: Any | None = ..., parameters: Any | None = ..., max_retries=..., status_retries=..., aws_conn_id: Any | None = ..., region_name: Any | None = ..., **kwargs) -> None: ...
    def execute(self, context) -> None: ...
    def get_hook(self): ...
    def on_kill(self) -> None: ...
