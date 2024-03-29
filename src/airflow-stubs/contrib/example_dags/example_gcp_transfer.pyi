from airflow import models as models
from airflow.contrib.hooks.gcp_transfer_hook import ALREADY_EXISTING_IN_SINK as ALREADY_EXISTING_IN_SINK, AWS_S3_DATA_SOURCE as AWS_S3_DATA_SOURCE, BUCKET_NAME as BUCKET_NAME, DESCRIPTION as DESCRIPTION, FILTER_JOB_NAMES as FILTER_JOB_NAMES, FILTER_PROJECT_ID as FILTER_PROJECT_ID, GCS_DATA_SINK as GCS_DATA_SINK, GCS_DATA_SOURCE as GCS_DATA_SOURCE, GcpTransferJobsStatus as GcpTransferJobsStatus, GcpTransferOperationStatus as GcpTransferOperationStatus, PROJECT_ID as PROJECT_ID, SCHEDULE as SCHEDULE, SCHEDULE_END_DATE as SCHEDULE_END_DATE, SCHEDULE_START_DATE as SCHEDULE_START_DATE, START_TIME_OF_DAY as START_TIME_OF_DAY, STATUS as STATUS, TRANSFER_JOB as TRANSFER_JOB, TRANSFER_JOB_FIELD_MASK as TRANSFER_JOB_FIELD_MASK, TRANSFER_OPTIONS as TRANSFER_OPTIONS, TRANSFER_SPEC as TRANSFER_SPEC
from airflow.contrib.operators.gcp_transfer_operator import GcpTransferServiceJobCreateOperator as GcpTransferServiceJobCreateOperator, GcpTransferServiceJobDeleteOperator as GcpTransferServiceJobDeleteOperator, GcpTransferServiceJobUpdateOperator as GcpTransferServiceJobUpdateOperator, GcpTransferServiceOperationCancelOperator as GcpTransferServiceOperationCancelOperator, GcpTransferServiceOperationGetOperator as GcpTransferServiceOperationGetOperator, GcpTransferServiceOperationPauseOperator as GcpTransferServiceOperationPauseOperator, GcpTransferServiceOperationResumeOperator as GcpTransferServiceOperationResumeOperator, GcpTransferServiceOperationsListOperator as GcpTransferServiceOperationsListOperator
from airflow.contrib.sensors.gcp_transfer_sensor import GCPTransferServiceWaitForJobStatusSensor as GCPTransferServiceWaitForJobStatusSensor
from airflow.utils.dates import days_ago as days_ago
from typing import Any, Dict

GCP_PROJECT_ID: Any
GCP_DESCRIPTION: Any
GCP_TRANSFER_TARGET_BUCKET: Any
WAIT_FOR_OPERATION_POKE_INTERVAL: Any
GCP_TRANSFER_SOURCE_AWS_BUCKET: Any
GCP_TRANSFER_FIRST_TARGET_BUCKET: Any
GCP_TRANSFER_SECOND_TARGET_BUCKET: Any
aws_to_gcs_transfer_body: Any
gcs_to_gcs_transfer_body: Dict[str, Any]
update_body: Any
list_filter_dict: Any
default_args: Any
create_transfer_job_from_aws: Any
wait_for_operation_to_start: Any
pause_operation: Any
update_job: Any
list_operations: Any
get_operation: Any
resume_operation: Any
wait_for_operation_to_end: Any
job_time: Any
create_transfer_job_from_gcp: Any
wait_for_second_operation_to_start: Any
cancel_operation: Any
delete_transfer_from_aws_job: Any
delete_transfer_from_gcp_job: Any
