from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GoogleCloudStorageObjectSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    bucket: Any
    object: Any
    google_cloud_conn_id: Any
    delegate_to: Any
    def __init__(self, bucket, object, google_cloud_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...

def ts_function(context): ...

class GoogleCloudStorageObjectUpdatedSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    bucket: Any
    object: Any
    ts_func: Any
    google_cloud_conn_id: Any
    delegate_to: Any
    def __init__(self, bucket, object, ts_func=..., google_cloud_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...

class GoogleCloudStoragePrefixSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    bucket: Any
    prefix: Any
    google_cloud_conn_id: Any
    delegate_to: Any
    def __init__(self, bucket, prefix, google_cloud_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...

def get_time(): ...

class GoogleCloudStorageUploadSessionCompleteSensor(BaseSensorOperator):
    template_fields: Any
    ui_color: str
    bucket: Any
    prefix: Any
    inactivity_period: Any
    min_objects: Any
    previous_num_objects: Any
    inactivity_seconds: int
    allow_delete: Any
    google_cloud_conn_id: Any
    delegate_to: Any
    last_activity_time: Any
    def __init__(self, bucket, prefix, inactivity_period=..., min_objects: int = ..., previous_num_objects: int = ..., allow_delete: bool = ..., google_cloud_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def is_bucket_updated(self, current_num_objects): ...
    def poke(self, context): ...
