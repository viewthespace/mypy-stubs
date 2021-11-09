from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook as GoogleCloudBaseHook
from typing import Any

class BigtableHook(GoogleCloudBaseHook):
    def __init__(self, gcp_conn_id: str = ..., delegate_to: Any | None = ...) -> None: ...
    def get_instance(self, instance_id, project_id: Any | None = ...): ...
    def delete_instance(self, instance_id, project_id: Any | None = ...) -> None: ...
    def create_instance(self, instance_id, main_cluster_id, main_cluster_zone, project_id: Any | None = ..., replica_cluster_id: Any | None = ..., replica_cluster_zone: Any | None = ..., instance_display_name: Any | None = ..., instance_type=..., instance_labels: Any | None = ..., cluster_nodes: Any | None = ..., cluster_storage_type=..., timeout: Any | None = ...): ...
    @staticmethod
    def create_table(instance, table_id, initial_split_keys: Any | None = ..., column_families: Any | None = ...) -> None: ...
    def delete_table(self, instance_id, table_id, project_id: Any | None = ...) -> None: ...
    @staticmethod
    def update_cluster(instance, cluster_id, nodes) -> None: ...
    @staticmethod
    def get_column_families_for_table(instance, table_id): ...
    @staticmethod
    def get_cluster_states_for_table(instance, table_id): ...