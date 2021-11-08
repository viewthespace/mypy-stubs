from airflow.kubernetes.pod import Port as Port, Resources as Resources
from airflow.kubernetes.secret import Secret as Secret
from airflow.kubernetes.volume import Volume as Volume
from airflow.kubernetes.volume_mount import VolumeMount as VolumeMount
from typing import Any

api_client: Any

class Pod:
    image: Any
    envs: Any
    cmds: Any
    args: Any
    secrets: Any
    result: Any
    labels: Any
    name: Any
    ports: Any
    volumes: Any
    volume_mounts: Any
    node_selectors: Any
    namespace: Any
    image_pull_policy: Any
    image_pull_secrets: Any
    init_containers: Any
    service_account_name: Any
    resources: Any
    annotations: Any
    affinity: Any
    hostnetwork: Any
    tolerations: Any
    security_context: Any
    configmaps: Any
    pod_runtime_info_envs: Any
    dnspolicy: Any
    def __init__(self, image, envs, cmds, args: Any | None = ..., secrets: Any | None = ..., labels: Any | None = ..., node_selectors: Any | None = ..., name: Any | None = ..., ports: Any | None = ..., volumes: Any | None = ..., volume_mounts: Any | None = ..., namespace: str = ..., result: Any | None = ..., image_pull_policy: str = ..., image_pull_secrets: Any | None = ..., init_containers: Any | None = ..., service_account_name: Any | None = ..., resources: Any | None = ..., annotations: Any | None = ..., affinity: Any | None = ..., hostnetwork: bool = ..., tolerations: Any | None = ..., security_context: Any | None = ..., configmaps: Any | None = ..., pod_runtime_info_envs: Any | None = ..., dnspolicy: Any | None = ...) -> None: ...
    def to_v1_kubernetes_pod(self): ...
    def as_dict(self): ...
