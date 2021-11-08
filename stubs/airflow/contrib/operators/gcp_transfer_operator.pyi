from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.aws_hook import AwsHook as AwsHook
from airflow.contrib.hooks.gcp_transfer_hook import ACCESS_KEY_ID as ACCESS_KEY_ID, AWS_ACCESS_KEY as AWS_ACCESS_KEY, AWS_S3_DATA_SOURCE as AWS_S3_DATA_SOURCE, BUCKET_NAME as BUCKET_NAME, DAY as DAY, DESCRIPTION as DESCRIPTION, GCPTransferServiceHook as GCPTransferServiceHook, GCS_DATA_SINK as GCS_DATA_SINK, GCS_DATA_SOURCE as GCS_DATA_SOURCE, GcpTransferJobsStatus as GcpTransferJobsStatus, HOURS as HOURS, HTTP_DATA_SOURCE as HTTP_DATA_SOURCE, MINUTES as MINUTES, MONTH as MONTH, OBJECT_CONDITIONS as OBJECT_CONDITIONS, PROJECT_ID as PROJECT_ID, SCHEDULE as SCHEDULE, SCHEDULE_END_DATE as SCHEDULE_END_DATE, SCHEDULE_START_DATE as SCHEDULE_START_DATE, SECONDS as SECONDS, SECRET_ACCESS_KEY as SECRET_ACCESS_KEY, START_TIME_OF_DAY as START_TIME_OF_DAY, STATUS as STATUS, TRANSFER_OPTIONS as TRANSFER_OPTIONS, TRANSFER_SPEC as TRANSFER_SPEC, YEAR as YEAR
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class TransferJobPreprocessor:
    body: Any
    aws_conn_id: Any
    default_schedule: Any
    def __init__(self, body, aws_conn_id: str = ..., default_schedule: bool = ...) -> None: ...
    def process_body(self): ...

class TransferJobValidator:
    body: Any
    def __init__(self, body) -> None: ...
    def validate_body(self) -> None: ...

class GcpTransferServiceJobCreateOperator(BaseOperator):
    template_fields: Any
    body: Any
    aws_conn_id: Any
    gcp_conn_id: Any
    api_version: Any
    def __init__(self, body, aws_conn_id: str = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class GcpTransferServiceJobUpdateOperator(BaseOperator):
    template_fields: Any
    job_name: Any
    body: Any
    gcp_conn_id: Any
    api_version: Any
    aws_conn_id: Any
    def __init__(self, job_name, body, aws_conn_id: str = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class GcpTransferServiceJobDeleteOperator(BaseOperator):
    template_fields: Any
    job_name: Any
    project_id: Any
    gcp_conn_id: Any
    api_version: Any
    def __init__(self, job_name, gcp_conn_id: str = ..., api_version: str = ..., project_id: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class GcpTransferServiceOperationGetOperator(BaseOperator):
    template_fields: Any
    operation_name: Any
    gcp_conn_id: Any
    api_version: Any
    def __init__(self, operation_name, gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class GcpTransferServiceOperationsListOperator(BaseOperator):
    template_fields: Any
    filter: Any
    gcp_conn_id: Any
    api_version: Any
    def __init__(self, filter, gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class GcpTransferServiceOperationPauseOperator(BaseOperator):
    template_fields: Any
    operation_name: Any
    gcp_conn_id: Any
    api_version: Any
    def __init__(self, operation_name, gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class GcpTransferServiceOperationResumeOperator(BaseOperator):
    template_fields: Any
    operation_name: Any
    gcp_conn_id: Any
    api_version: Any
    def __init__(self, operation_name, gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class GcpTransferServiceOperationCancelOperator(BaseOperator):
    template_fields: Any
    operation_name: Any
    api_version: Any
    gcp_conn_id: Any
    def __init__(self, operation_name, api_version: str = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class S3ToGoogleCloudStorageTransferOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    s3_bucket: Any
    gcs_bucket: Any
    project_id: Any
    aws_conn_id: Any
    gcp_conn_id: Any
    delegate_to: Any
    description: Any
    schedule: Any
    object_conditions: Any
    transfer_options: Any
    wait: Any
    timeout: Any
    def __init__(self, s3_bucket, gcs_bucket, project_id: Any | None = ..., aws_conn_id: str = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., description: Any | None = ..., schedule: Any | None = ..., object_conditions: Any | None = ..., transfer_options: Any | None = ..., wait: bool = ..., timeout: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class GoogleCloudStorageToGoogleCloudStorageTransferOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    source_bucket: Any
    destination_bucket: Any
    project_id: Any
    gcp_conn_id: Any
    delegate_to: Any
    description: Any
    schedule: Any
    object_conditions: Any
    transfer_options: Any
    wait: Any
    timeout: Any
    def __init__(self, source_bucket, destination_bucket, project_id: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., description: Any | None = ..., schedule: Any | None = ..., object_conditions: Any | None = ..., transfer_options: Any | None = ..., wait: bool = ..., timeout: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
