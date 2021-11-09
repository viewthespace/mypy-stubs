from airflow.configuration import conf as conf
from airflow.kubernetes.refresh_config import RefreshConfiguration as RefreshConfiguration, load_kube_config as load_kube_config
from kubernetes.client import Configuration as Configuration
from typing import Optional

has_kubernetes: bool
ApiException = BaseException

def get_kube_client(in_cluster: bool = ..., cluster_context: Optional[str] = ..., config_file: Optional[str] = ...): ...
