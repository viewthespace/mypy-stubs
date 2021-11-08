from airflow.exceptions import AirflowException as AirflowException
from airflow.kubernetes import kube_client as kube_client, pod_generator as pod_generator, pod_launcher as pod_launcher
from airflow.kubernetes.k8s_model import append_to_pod as append_to_pod
from airflow.kubernetes.pod import Resources as Resources
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.helpers import validate_key as validate_key
from airflow.utils.state import State as State
from typing import Any

class KubernetesPodOperator(BaseOperator):
    template_fields: Any
    pod: Any
    do_xcom_push: Any
    image: Any
    namespace: Any
    cmds: Any
    arguments: Any
    labels: Any
    startup_timeout_seconds: Any
    env_vars: Any
    ports: Any
    volume_mounts: Any
    volumes: Any
    secrets: Any
    in_cluster: Any
    cluster_context: Any
    reattach_on_restart: Any
    get_logs: Any
    image_pull_policy: Any
    node_selectors: Any
    annotations: Any
    affinity: Any
    resources: Any
    config_file: Any
    image_pull_secrets: Any
    service_account_name: Any
    is_delete_operator_pod: Any
    hostnetwork: Any
    tolerations: Any
    configmaps: Any
    security_context: Any
    pod_runtime_info_envs: Any
    dnspolicy: Any
    schedulername: Any
    full_pod_spec: Any
    init_containers: Any
    log_events_on_failure: Any
    pod_template_file: Any
    priority_class_name: Any
    name: Any
    def __init__(self, namespace: Any | None = ..., image: Any | None = ..., name: Any | None = ..., cmds: Any | None = ..., arguments: Any | None = ..., ports: Any | None = ..., volume_mounts: Any | None = ..., volumes: Any | None = ..., env_vars: Any | None = ..., secrets: Any | None = ..., in_cluster: Any | None = ..., cluster_context: Any | None = ..., labels: Any | None = ..., reattach_on_restart: bool = ..., startup_timeout_seconds: int = ..., get_logs: bool = ..., image_pull_policy: str = ..., annotations: Any | None = ..., resources: Any | None = ..., affinity: Any | None = ..., config_file: Any | None = ..., node_selectors: Any | None = ..., image_pull_secrets: Any | None = ..., service_account_name: str = ..., is_delete_operator_pod: bool = ..., hostnetwork: bool = ..., tolerations: Any | None = ..., configmaps: Any | None = ..., security_context: Any | None = ..., pod_runtime_info_envs: Any | None = ..., dnspolicy: Any | None = ..., schedulername: Any | None = ..., full_pod_spec: Any | None = ..., init_containers: Any | None = ..., log_events_on_failure: bool = ..., do_xcom_push: bool = ..., pod_template_file: Any | None = ..., priority_class_name: Any | None = ..., *args, **kwargs) -> None: ...
    @staticmethod
    def create_labels_for_pod(context): ...
    def execute(self, context): ...
    def handle_pod_overlap(self, labels, try_numbers_match, launcher, pod_list): ...
    def create_new_pod_for_operator(self, labels, launcher): ...
    def monitor_launched_pod(self, launcher, pod): ...
