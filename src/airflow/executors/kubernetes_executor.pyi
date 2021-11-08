import multiprocessing
from airflow import settings as settings
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException, AirflowException as AirflowException
from airflow.executors.base_executor import BaseExecutor as BaseExecutor
from airflow.kubernetes import pod_generator as pod_generator
from airflow.kubernetes.kube_client import get_kube_client as get_kube_client
from airflow.kubernetes.pod_generator import MAX_POD_ID_LEN as MAX_POD_ID_LEN, PodGenerator as PodGenerator
from airflow.kubernetes.pod_launcher import PodLauncher as PodLauncher
from airflow.kubernetes.worker_configuration import WorkerConfiguration as WorkerConfiguration
from airflow.models import KubeResourceVersion as KubeResourceVersion, KubeWorkerIdentifier as KubeWorkerIdentifier, TaskInstance as TaskInstance
from airflow.utils.db import create_session as create_session, provide_session as provide_session
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.state import State as State
from typing import Any

class KubeConfig:
    core_section: str
    kubernetes_section: str
    core_configuration: Any
    kube_secrets: Any
    kube_env_vars: Any
    env_from_configmap_ref: Any
    env_from_secret_ref: Any
    airflow_home: Any
    dags_folder: Any
    parallelism: Any
    worker_container_repository: Any
    worker_container_tag: Any
    kube_image: Any
    kube_image_pull_policy: Any
    kube_node_selectors: Any
    kube_annotations: Any
    pod_template_file: Any
    kube_labels: Any
    delete_worker_pods: Any
    delete_worker_pods_on_failure: Any
    worker_pods_creation_batch_size: Any
    worker_service_account_name: Any
    image_pull_secrets: Any
    dags_in_image: Any
    worker_run_as_user: Any
    worker_fs_group: Any
    git_repo: Any
    git_branch: Any
    git_sync_depth: Any
    git_subpath: Any
    git_sync_root: Any
    git_sync_dest: Any
    git_sync_rev: Any
    git_dags_folder_mount_point: Any
    git_user: Any
    git_password: Any
    git_ssh_key_secret_name: Any
    git_ssh_known_hosts_configmap_name: Any
    git_sync_credentials_secret: Any
    dags_volume_claim: Any
    dags_volume_mount_point: Any
    logs_volume_claim: Any
    dags_volume_subpath: Any
    logs_volume_subpath: Any
    dags_volume_host: Any
    logs_volume_host: Any
    base_log_folder: Any
    kube_namespace: Any
    multi_namespace_mode: Any
    executor_namespace: Any
    gcp_service_account_keys: Any
    git_sync_container_repository: Any
    git_sync_container_tag: Any
    git_sync_container: Any
    git_sync_init_container_name: Any
    git_sync_run_as_user: Any
    airflow_configmap: Any
    airflow_local_settings_configmap: Any
    kube_affinity: Any
    kube_tolerations: Any
    kube_client_request_args: Any
    delete_option_kwargs: Any
    def __init__(self) -> None: ...

class KubernetesJobWatcher(multiprocessing.Process, LoggingMixin):
    namespace: Any
    multi_namespace_mode: Any
    worker_uuid: Any
    watcher_queue: Any
    resource_version: Any
    kube_config: Any
    def __init__(self, namespace, multi_namespace_mode, watcher_queue, resource_version, worker_uuid, kube_config) -> None: ...
    def run(self) -> None: ...
    def process_error(self, event): ...
    def process_status(self, pod_id, namespace, status, labels, resource_version, event) -> None: ...

class AirflowKubernetesScheduler(LoggingMixin):
    kube_config: Any
    task_queue: Any
    result_queue: Any
    namespace: Any
    kube_client: Any
    launcher: Any
    worker_configuration_pod: Any
    watcher_queue: Any
    worker_uuid: Any
    kube_watcher: Any
    def __init__(self, kube_config, task_queue, result_queue, kube_client, worker_uuid) -> None: ...
    def run_next(self, next_job) -> None: ...
    def delete_pod(self, pod_id, namespace) -> None: ...
    def sync(self) -> None: ...
    def process_watcher_task(self, task) -> None: ...
    def terminate(self) -> None: ...

class KubernetesExecutor(BaseExecutor, LoggingMixin):
    kube_config: Any
    task_queue: Any
    result_queue: Any
    kube_scheduler: Any
    kube_client: Any
    worker_uuid: Any
    def __init__(self) -> None: ...
    def clear_not_launched_queued_tasks(self, session: Any | None = ...) -> None: ...
    def start(self) -> None: ...
    def execute_async(self, key, command, queue: Any | None = ..., executor_config: Any | None = ...) -> None: ...
    def sync(self) -> None: ...
    def end(self) -> None: ...
