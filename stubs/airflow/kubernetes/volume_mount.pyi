from airflow.kubernetes.k8s_model import K8SModel as K8SModel
from typing import Any

class VolumeMount(K8SModel):
    name: Any
    mount_path: Any
    sub_path: Any
    read_only: Any
    def __init__(self, name, mount_path, sub_path, read_only) -> None: ...
    def to_k8s_client_obj(self): ...
    def attach_to_pod(self, pod): ...
