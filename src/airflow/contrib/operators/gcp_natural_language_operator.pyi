from airflow.contrib.hooks.gcp_natural_language_hook import CloudNaturalLanguageHook as CloudNaturalLanguageHook
from airflow.models import BaseOperator as BaseOperator
from typing import Any

class CloudLanguageAnalyzeEntitiesOperator(BaseOperator):
    template_fields: Any
    document: Any
    encoding_type: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, document, encoding_type: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudLanguageAnalyzeEntitySentimentOperator(BaseOperator):
    template_fields: Any
    document: Any
    encoding_type: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, document, encoding_type: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudLanguageAnalyzeSentimentOperator(BaseOperator):
    template_fields: Any
    document: Any
    encoding_type: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, document, encoding_type: Any | None = ..., retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudLanguageClassifyTextOperator(BaseOperator):
    template_fields: Any
    document: Any
    retry: Any
    timeout: Any
    metadata: Any
    gcp_conn_id: Any
    def __init__(self, document, retry: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
