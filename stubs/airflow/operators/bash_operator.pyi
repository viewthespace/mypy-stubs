from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.file import TemporaryDirectory as TemporaryDirectory
from airflow.utils.operator_helpers import context_to_airflow_vars as context_to_airflow_vars
from typing import Any

class BashOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    bash_command: Any
    env: Any
    xcom_push_flag: Any
    output_encoding: Any
    sub_process: Any
    def __init__(self, bash_command, xcom_push: bool = ..., env: Any | None = ..., output_encoding: str = ..., *args, **kwargs) -> None: ...
    lineage_data: Any
    def execute(self, context): ...
    def on_kill(self) -> None: ...
