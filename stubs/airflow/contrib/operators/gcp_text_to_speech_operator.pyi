from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_text_to_speech_hook import GCPTextToSpeechHook as GCPTextToSpeechHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GcpTextToSpeechSynthesizeOperator(BaseOperator):
    template_fields: Any
    input_data: Any
    voice: Any
    audio_config: Any
    target_bucket_name: Any
    target_filename: Any
    project_id: Any
    gcp_conn_id: Any
    retry: Any
    timeout: Any
    def __init__(self, input_data, voice, audio_config, target_bucket_name, target_filename, project_id: Any | None = ..., gcp_conn_id: str = ..., retry: Any | None = ..., timeout: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
