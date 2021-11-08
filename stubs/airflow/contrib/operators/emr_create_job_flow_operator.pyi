from airflow.contrib.hooks.emr_hook import EmrHook as EmrHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils import apply_defaults as apply_defaults
from typing import Any

class EmrCreateJobFlowOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    aws_conn_id: Any
    emr_conn_id: Any
    job_flow_overrides: Any
    region_name: Any
    def __init__(self, aws_conn_id: str = ..., emr_conn_id: str = ..., job_flow_overrides: Any | None = ..., region_name: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
