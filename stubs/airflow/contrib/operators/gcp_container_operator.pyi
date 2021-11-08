from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_container_hook import GKEClusterHook as GKEClusterHook
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator as KubernetesPodOperator
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class GKEClusterDeleteOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    gcp_conn_id: Any
    location: Any
    api_version: Any
    name: Any
    def __init__(self, project_id, name, location, gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class GKEClusterCreateOperator(BaseOperator):
    template_fields: Any
    project_id: Any
    gcp_conn_id: Any
    location: Any
    api_version: Any
    body: Any
    def __init__(self, project_id, location, body: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

KUBE_CONFIG_ENV_VAR: str

class GKEPodOperator(KubernetesPodOperator):
    template_fields: Any
    project_id: Any
    location: Any
    cluster_name: Any
    gcp_conn_id: Any
    def __init__(self, project_id, location, cluster_name, gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    config_file: Any
    def execute(self, context) -> None: ...
