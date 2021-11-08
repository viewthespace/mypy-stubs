from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_speech_to_text_hook import GCPSpeechToTextHook as GCPSpeechToTextHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GcpSpeechToTextRecognizeSpeechOperator(BaseOperator):
    template_fields: Any
    audio: Any
    config: Any
    project_id: Any
    gcp_conn_id: Any
    retry: Any
    timeout: Any
    def __init__(self, audio, config, project_id: Any | None = ..., gcp_conn_id: str = ..., retry: Any | None = ..., timeout: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
