from airflow.configuration import conf as conf
from typing import Any

log: Any
CLIENT_AUTH: Any

class KerberosService:
    service_name: Any
    def __init__(self) -> None: ...

def init_app(app) -> None: ...
def requires_authentication(function): ...
