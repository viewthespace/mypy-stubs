from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook as GoogleCloudBaseHook
from airflow.exceptions import AirflowException as AirflowException
from typing import Any

TIME_TO_SLEEP_IN_SECONDS: int

class GcpTransferJobsStatus:
    ENABLED: str
    DISABLED: str
    DELETED: str

class GcpTransferOperationStatus:
    IN_PROGRESS: str
    PAUSED: str
    SUCCESS: str
    FAILED: str
    ABORTED: str

ACCESS_KEY_ID: str
ALREADY_EXISTING_IN_SINK: str
AWS_ACCESS_KEY: str
AWS_S3_DATA_SOURCE: str
BODY: str
BUCKET_NAME: str
DAY: str
DESCRIPTION: str
FILTER: str
FILTER_JOB_NAMES: str
FILTER_PROJECT_ID: str
GCS_DATA_SINK: str
GCS_DATA_SOURCE: str
HOURS: str
HTTP_DATA_SOURCE: str
LIST_URL: str
METADATA: str
MINUTES: str
MONTH: str
NAME: str
OBJECT_CONDITIONS: str
OPERATIONS: str
PROJECT_ID: str
SCHEDULE: str
SCHEDULE_END_DATE: str
SCHEDULE_START_DATE: str
SECONDS: str
SECRET_ACCESS_KEY: str
START_TIME_OF_DAY: str
STATUS: str
STATUS1: str
TRANSFER_JOB: str
TRANSFER_JOB_FIELD_MASK: str
TRANSFER_JOBS: str
TRANSFER_OPERATIONS: str
TRANSFER_OPTIONS: str
TRANSFER_SPEC: str
YEAR: str
NEGATIVE_STATUSES: Any

class GCPTransferServiceHook(GoogleCloudBaseHook):
    api_version: Any
    def __init__(self, api_version: str = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ...) -> None: ...
    def get_conn(self): ...
    def create_transfer_job(self, body): ...
    def get_transfer_job(self, job_name, project_id: Any | None = ...): ...
    def list_transfer_job(self, filter): ...
    def update_transfer_job(self, job_name, body): ...
    def delete_transfer_job(self, job_name, project_id): ...
    def cancel_transfer_operation(self, operation_name) -> None: ...
    def get_transfer_operation(self, operation_name): ...
    def list_transfer_operations(self, filter): ...
    def pause_transfer_operation(self, operation_name) -> None: ...
    def resume_transfer_operation(self, operation_name) -> None: ...
    def wait_for_transfer_job(self, job, expected_statuses=..., timeout: int = ...) -> None: ...
    @staticmethod
    def operations_contain_expected_statuses(operations, expected_statuses): ...
