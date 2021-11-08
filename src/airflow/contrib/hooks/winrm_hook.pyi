from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class WinRMHook(BaseHook):
    ssh_conn_id: Any
    endpoint: Any
    remote_host: Any
    remote_port: Any
    transport: Any
    username: Any
    password: Any
    service: Any
    keytab: Any
    ca_trust_path: Any
    cert_pem: Any
    cert_key_pem: Any
    server_cert_validation: Any
    kerberos_delegation: Any
    read_timeout_sec: Any
    operation_timeout_sec: Any
    kerberos_hostname_override: Any
    message_encryption: Any
    credssp_disable_tlsv1_2: Any
    send_cbt: Any
    client: Any
    winrm_protocol: Any
    def __init__(self, ssh_conn_id: Any | None = ..., endpoint: Any | None = ..., remote_host: Any | None = ..., remote_port: int = ..., transport: str = ..., username: Any | None = ..., password: Any | None = ..., service: str = ..., keytab: Any | None = ..., ca_trust_path: Any | None = ..., cert_pem: Any | None = ..., cert_key_pem: Any | None = ..., server_cert_validation: str = ..., kerberos_delegation: bool = ..., read_timeout_sec: int = ..., operation_timeout_sec: int = ..., kerberos_hostname_override: Any | None = ..., message_encryption: str = ..., credssp_disable_tlsv1_2: bool = ..., send_cbt: bool = ...) -> None: ...
    def get_conn(self): ...
