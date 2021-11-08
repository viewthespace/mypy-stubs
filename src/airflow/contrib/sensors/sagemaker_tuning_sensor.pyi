from airflow.contrib.hooks.sagemaker_hook import SageMakerHook as SageMakerHook
from airflow.contrib.sensors.sagemaker_base_sensor import SageMakerBaseSensor as SageMakerBaseSensor
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SageMakerTuningSensor(SageMakerBaseSensor):
    template_fields: Any
    template_ext: Any
    job_name: Any
    def __init__(self, job_name, *args, **kwargs) -> None: ...
    def non_terminal_states(self): ...
    def failed_states(self): ...
    def get_sagemaker_response(self): ...
    def get_failed_reason_from_response(self, response): ...
    def state_from_response(self, response): ...