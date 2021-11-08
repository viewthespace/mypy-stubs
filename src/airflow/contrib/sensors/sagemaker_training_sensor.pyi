from airflow.contrib.hooks.sagemaker_hook import LogState as LogState, SageMakerHook as SageMakerHook
from airflow.contrib.sensors.sagemaker_base_sensor import SageMakerBaseSensor as SageMakerBaseSensor
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SageMakerTrainingSensor(SageMakerBaseSensor):
    template_fields: Any
    template_ext: Any
    job_name: Any
    print_log: Any
    positions: Any
    stream_names: Any
    instance_count: Any
    state: Any
    last_description: Any
    last_describe_job_call: Any
    log_resource_inited: bool
    def __init__(self, job_name, print_log: bool = ..., *args, **kwargs) -> None: ...
    def init_log_resource(self, hook) -> None: ...
    def non_terminal_states(self): ...
    def failed_states(self): ...
    def get_sagemaker_response(self): ...
    def get_failed_reason_from_response(self, response): ...
    def state_from_response(self, response): ...
