from airflow.contrib.hooks.emr_hook import EmrHook as EmrHook
from airflow.contrib.sensors.emr_base_sensor import EmrBaseSensor as EmrBaseSensor
from airflow.utils import apply_defaults as apply_defaults
from typing import Any

class EmrStepSensor(EmrBaseSensor):
    NON_TERMINAL_STATES: Any
    FAILED_STATE: Any
    template_fields: Any
    template_ext: Any
    job_flow_id: Any
    step_id: Any
    def __init__(self, job_flow_id, step_id, *args, **kwargs) -> None: ...
    def get_emr_response(self): ...
    @staticmethod
    def state_from_response(response): ...
    @staticmethod
    def failure_message_from_response(response): ...
