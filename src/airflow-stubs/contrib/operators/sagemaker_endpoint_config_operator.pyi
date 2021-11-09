from airflow.contrib.operators.sagemaker_base_operator import SageMakerBaseOperator as SageMakerBaseOperator
from airflow.exceptions import AirflowException as AirflowException
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SageMakerEndpointConfigOperator(SageMakerBaseOperator):
    integer_fields: Any
    config: Any
    def __init__(self, config, *args, **kwargs) -> None: ...
    def execute(self, context): ...
