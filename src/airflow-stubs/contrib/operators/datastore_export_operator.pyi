from airflow.contrib.hooks.datastore_hook import DatastoreHook as DatastoreHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class DatastoreExportOperator(BaseOperator):
    datastore_conn_id: Any
    cloud_storage_conn_id: Any
    delegate_to: Any
    bucket: Any
    namespace: Any
    entity_filter: Any
    labels: Any
    polling_interval_in_seconds: Any
    overwrite_existing: Any
    xcom_push: Any
    def __init__(self, bucket, namespace: Any | None = ..., datastore_conn_id: str = ..., cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., entity_filter: Any | None = ..., labels: Any | None = ..., polling_interval_in_seconds: int = ..., overwrite_existing: bool = ..., xcom_push: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
