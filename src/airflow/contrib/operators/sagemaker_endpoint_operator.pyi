from airflow.contrib.hooks.aws_hook import AwsHook as AwsHook
from airflow.contrib.operators.sagemaker_base_operator import SageMakerBaseOperator as SageMakerBaseOperator
from airflow.exceptions import AirflowException as AirflowException
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SageMakerEndpointOperator(SageMakerBaseOperator):
    config: Any
    wait_for_completion: Any
    check_interval: Any
    max_ingestion_time: Any
    operation: Any
    def __init__(self, config, wait_for_completion: bool = ..., check_interval: int = ..., max_ingestion_time: Any | None = ..., operation: str = ..., *args, **kwargs) -> None: ...
    integer_fields: Any
    def create_integer_fields(self) -> None: ...
    def expand_role(self) -> None: ...
    def execute(self, context): ...
