from airflow.contrib.hooks.emr_hook import EmrHook as EmrHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils import apply_defaults as apply_defaults
from typing import Any

class EmrAddStepsOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    aws_conn_id: Any
    job_flow_id: Any
    job_flow_name: Any
    cluster_states: Any
    steps: Any
    def __init__(self, job_flow_id: Any | None = ..., job_flow_name: Any | None = ..., cluster_states: Any | None = ..., aws_conn_id: str = ..., steps: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
