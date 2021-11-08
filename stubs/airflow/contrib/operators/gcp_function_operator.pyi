from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_function_hook import GcfHook as GcfHook
from airflow.contrib.utils.gcp_field_validator import GcpBodyFieldValidator as GcpBodyFieldValidator, GcpFieldValidationException as GcpFieldValidationException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.version import version as version
from typing import Any

CLOUD_FUNCTION_VALIDATION: Any

class GcfFunctionDeployOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    location: Any
    body: Any
    gcp_conn_id: Any
    api_version: Any
    zip_path: Any
    zip_path_preprocessor: Any
    def __init__(self, location, body, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., zip_path: Any | None = ..., validate_body: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

GCF_SOURCE_ARCHIVE_URL: str
GCF_SOURCE_UPLOAD_URL: str
SOURCE_REPOSITORY: str
GCF_ZIP_PATH: str

class ZipPathPreprocessor:
    upload_function: Any
    body: Any
    zip_path: Any
    def __init__(self, body, zip_path) -> None: ...
    def should_upload_function(self): ...
    def preprocess_body(self) -> None: ...

FUNCTION_NAME_PATTERN: str
FUNCTION_NAME_COMPILED_PATTERN: Any

class GcfFunctionDeleteOperator(BaseOperator):
    template_fields: Any
    name: Any
    gcp_conn_id: Any
    api_version: Any
    hook: Any
    def __init__(self, name, gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
