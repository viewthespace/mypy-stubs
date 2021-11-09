from airflow.contrib.hooks.azure_container_instance_hook import AzureContainerInstanceHook as AzureContainerInstanceHook
from airflow.contrib.hooks.azure_container_registry_hook import AzureContainerRegistryHook as AzureContainerRegistryHook
from airflow.contrib.hooks.azure_container_volume_hook import AzureContainerVolumeHook as AzureContainerVolumeHook
from airflow.exceptions import AirflowException as AirflowException, AirflowTaskTimeout as AirflowTaskTimeout
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any, Dict, NamedTuple, Sequence

class Volume(NamedTuple):
    conn_id: Any
    account_name: Any
    share_name: Any
    mount_path: Any
    read_only: Any
DEFAULT_ENVIRONMENT_VARIABLES: Dict[str, str]
DEFAULT_SECURED_VARIABLES: Sequence[str]
DEFAULT_VOLUMES: Sequence[Volume]
DEFAULT_MEMORY_IN_GB: float
DEFAULT_CPU: float

class AzureContainerInstancesOperator(BaseOperator):
    template_fields: Any
    ci_conn_id: Any
    resource_group: Any
    name: Any
    image: Any
    region: Any
    registry_conn_id: Any
    environment_variables: Any
    secured_variables: Any
    volumes: Any
    memory_in_gb: Any
    cpu: Any
    gpu: Any
    command: Any
    remove_on_error: Any
    fail_if_exists: Any
    tags: Any
    def __init__(self, ci_conn_id, registry_conn_id, resource_group, name, image, region, environment_variables: Any | None = ..., secured_variables: Any | None = ..., volumes: Any | None = ..., memory_in_gb: Any | None = ..., cpu: Any | None = ..., gpu: Any | None = ..., command: Any | None = ..., remove_on_error: bool = ..., fail_if_exists: bool = ..., tags: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
    def on_kill(self) -> None: ...
