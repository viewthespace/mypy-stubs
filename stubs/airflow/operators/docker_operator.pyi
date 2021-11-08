from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.docker_hook import DockerHook as DockerHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.file import TemporaryDirectory as TemporaryDirectory
from typing import Any

class DockerOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    api_version: Any
    auto_remove: Any
    command: Any
    container_name: Any
    cpus: Any
    dns: Any
    dns_search: Any
    docker_url: Any
    environment: Any
    force_pull: Any
    image: Any
    mem_limit: Any
    host_tmp_dir: Any
    network_mode: Any
    tls_ca_cert: Any
    tls_client_cert: Any
    tls_client_key: Any
    tls_hostname: Any
    tls_ssl_version: Any
    tmp_dir: Any
    user: Any
    volumes: Any
    working_dir: Any
    xcom_push_flag: Any
    xcom_all: Any
    docker_conn_id: Any
    shm_size: Any
    tty: Any
    cli: Any
    container: Any
    def __init__(self, image, api_version: Any | None = ..., command: Any | None = ..., container_name: Any | None = ..., cpus: float = ..., docker_url: str = ..., environment: Any | None = ..., force_pull: bool = ..., mem_limit: Any | None = ..., host_tmp_dir: Any | None = ..., network_mode: Any | None = ..., tls_ca_cert: Any | None = ..., tls_client_cert: Any | None = ..., tls_client_key: Any | None = ..., tls_hostname: Any | None = ..., tls_ssl_version: Any | None = ..., tmp_dir: str = ..., user: Any | None = ..., volumes: Any | None = ..., working_dir: Any | None = ..., xcom_push: bool = ..., xcom_all: bool = ..., docker_conn_id: Any | None = ..., dns: Any | None = ..., dns_search: Any | None = ..., auto_remove: bool = ..., shm_size: Any | None = ..., tty: bool = ..., *args, **kwargs) -> None: ...
    def get_hook(self): ...
    def execute(self, context): ...
    def get_command(self): ...
    def on_kill(self) -> None: ...
