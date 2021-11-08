from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GoogleCloudStorageBucketCreateAclEntryOperator(BaseOperator):
    template_fields: Any
    bucket: Any
    entity: Any
    role: Any
    user_project: Any
    google_cloud_storage_conn_id: Any
    def __init__(self, bucket, entity, role, user_project: Any | None = ..., google_cloud_storage_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class GoogleCloudStorageObjectCreateAclEntryOperator(BaseOperator):
    template_fields: Any
    bucket: Any
    object_name: Any
    entity: Any
    role: Any
    generation: Any
    user_project: Any
    google_cloud_storage_conn_id: Any
    def __init__(self, bucket, object_name, entity, role, generation: Any | None = ..., user_project: Any | None = ..., google_cloud_storage_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
