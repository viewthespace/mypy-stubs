from airflow.contrib.hooks.emr_hook import EmrHook as EmrHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils import apply_defaults as apply_defaults
from typing import Any

class EmrTerminateJobFlowOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    job_flow_id: Any
    aws_conn_id: Any
    def __init__(self, job_flow_id, aws_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
