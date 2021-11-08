from airflow.configuration import conf as conf
from airflow.kubernetes.k8s_model import append_to_pod as append_to_pod
from airflow.kubernetes.pod_generator import PodGenerator as PodGenerator
from airflow.kubernetes.secret import Secret as Secret
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

class WorkerConfiguration(LoggingMixin):
    dags_volume_name: str
    logs_volume_name: str
    git_sync_ssh_secret_volume_name: str
    git_ssh_key_secret_key: str
    git_sync_ssh_known_hosts_volume_name: str
    git_ssh_known_hosts_configmap_key: str
    kube_config: Any
    worker_airflow_home: Any
    worker_airflow_dags: Any
    worker_airflow_logs: Any
    def __init__(self, kube_config) -> None: ...
    def generate_dag_volume_mount_path(self): ...
    def as_pod(self): ...
