from airflow.contrib.hooks.gcp_video_intelligence_hook import CloudVideoIntelligenceHook as CloudVideoIntelligenceHook
from airflow.models import BaseOperator as BaseOperator
from typing import Any

class CloudVideoIntelligenceDetectVideoLabelsOperator(BaseOperator):
    template_fields: Any
    input_uri: Any
    input_content: Any
    output_uri: Any
    video_context: Any
    location: Any
    retry: Any
    gcp_conn_id: Any
    timeout: Any
    def __init__(self, input_uri, input_content: Any | None = ..., output_uri: Any | None = ..., video_context: Any | None = ..., location: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVideoIntelligenceDetectVideoExplicitContentOperator(BaseOperator):
    template_fields: Any
    input_uri: Any
    output_uri: Any
    input_content: Any
    video_context: Any
    location: Any
    retry: Any
    gcp_conn_id: Any
    timeout: Any
    def __init__(self, input_uri, output_uri: Any | None = ..., input_content: Any | None = ..., video_context: Any | None = ..., location: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudVideoIntelligenceDetectVideoShotsOperator(BaseOperator):
    template_fields: Any
    input_uri: Any
    output_uri: Any
    input_content: Any
    video_context: Any
    location: Any
    retry: Any
    gcp_conn_id: Any
    timeout: Any
    def __init__(self, input_uri, output_uri: Any | None = ..., input_content: Any | None = ..., video_context: Any | None = ..., location: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
