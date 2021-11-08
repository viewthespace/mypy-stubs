from airflow.contrib.hooks.datastore_hook import DatastoreHook as DatastoreHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class DatastoreImportOperator(BaseOperator):
    datastore_conn_id: Any
    delegate_to: Any
    bucket: Any
    file: Any
    namespace: Any
    entity_filter: Any
    labels: Any
    polling_interval_in_seconds: Any
    xcom_push: Any
    def __init__(self, bucket, file, namespace: Any | None = ..., entity_filter: Any | None = ..., labels: Any | None = ..., datastore_conn_id: str = ..., delegate_to: Any | None = ..., polling_interval_in_seconds: int = ..., xcom_push: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
