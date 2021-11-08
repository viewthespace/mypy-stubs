from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_bigtable_hook import BigtableHook as BigtableHook
from airflow.models import BaseOperator as BaseOperator
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any, Iterable

class BigtableValidationMixin:
    REQUIRED_ATTRIBUTES: Iterable[str]

class BigtableInstanceCreateOperator(BaseOperator, BigtableValidationMixin):
    REQUIRED_ATTRIBUTES: Any
    template_fields: Any
    project_id: Any
    instance_id: Any
    main_cluster_id: Any
    main_cluster_zone: Any
    replica_cluster_id: Any
    replica_cluster_zone: Any
    instance_display_name: Any
    instance_type: Any
    instance_labels: Any
    cluster_nodes: Any
    cluster_storage_type: Any
    timeout: Any
    hook: Any
    def __init__(self, instance_id, main_cluster_id, main_cluster_zone, project_id: Any | None = ..., replica_cluster_id: Any | None = ..., replica_cluster_zone: Any | None = ..., instance_display_name: Any | None = ..., instance_type: Any | None = ..., instance_labels: Any | None = ..., cluster_nodes: Any | None = ..., cluster_storage_type: Any | None = ..., timeout: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class BigtableInstanceDeleteOperator(BaseOperator, BigtableValidationMixin):
    REQUIRED_ATTRIBUTES: Any
    template_fields: Any
    project_id: Any
    instance_id: Any
    hook: Any
    def __init__(self, instance_id, project_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class BigtableTableCreateOperator(BaseOperator, BigtableValidationMixin):
    REQUIRED_ATTRIBUTES: Any
    template_fields: Any
    project_id: Any
    instance_id: Any
    table_id: Any
    initial_split_keys: Any
    column_families: Any
    hook: Any
    instance: Any
    def __init__(self, instance_id, table_id, project_id: Any | None = ..., initial_split_keys: Any | None = ..., column_families: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class BigtableTableDeleteOperator(BaseOperator, BigtableValidationMixin):
    REQUIRED_ATTRIBUTES: Any
    template_fields: Any
    project_id: Any
    instance_id: Any
    table_id: Any
    app_profile_id: Any
    hook: Any
    def __init__(self, instance_id, table_id, project_id: Any | None = ..., app_profile_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class BigtableClusterUpdateOperator(BaseOperator, BigtableValidationMixin):
    REQUIRED_ATTRIBUTES: Any
    template_fields: Any
    project_id: Any
    instance_id: Any
    cluster_id: Any
    nodes: Any
    hook: Any
    def __init__(self, instance_id, cluster_id, nodes, project_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class BigtableTableWaitForReplicationSensor(BaseSensorOperator, BigtableValidationMixin):
    REQUIRED_ATTRIBUTES: Any
    template_fields: Any
    project_id: Any
    instance_id: Any
    table_id: Any
    hook: Any
    def __init__(self, instance_id, table_id, project_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
