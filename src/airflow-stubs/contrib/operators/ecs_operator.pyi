from airflow.contrib.hooks.aws_hook import AwsHook as AwsHook
from airflow.contrib.hooks.aws_logs_hook import AwsLogsHook as AwsLogsHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils import apply_defaults as apply_defaults
from typing import Any

class ECSOperator(BaseOperator):
    ui_color: str
    client: Any
    arn: Any
    template_fields: Any
    aws_conn_id: Any
    region_name: Any
    task_definition: Any
    cluster: Any
    overrides: Any
    launch_type: Any
    group: Any
    placement_constraints: Any
    platform_version: Any
    network_configuration: Any
    tags: Any
    awslogs_group: Any
    awslogs_stream_prefix: Any
    awslogs_region: Any
    hook: Any
    def __init__(self, task_definition, cluster, overrides, aws_conn_id: Any | None = ..., region_name: Any | None = ..., launch_type: str = ..., group: Any | None = ..., placement_constraints: Any | None = ..., platform_version: str = ..., network_configuration: Any | None = ..., tags: Any | None = ..., awslogs_group: Any | None = ..., awslogs_region: Any | None = ..., awslogs_stream_prefix: Any | None = ..., **kwargs) -> None: ...
    def execute(self, context) -> None: ...
    def get_hook(self): ...
    def get_logs_hook(self): ...
    def on_kill(self) -> None: ...
