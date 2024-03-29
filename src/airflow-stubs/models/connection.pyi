from airflow import LoggingMixin as LoggingMixin
from airflow.exceptions import AirflowException as AirflowException
from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.models.crypto import get_fernet as get_fernet
from typing import Any

def parse_netloc_to_hostname(uri_parts): ...

class Connection(Base, LoggingMixin):
    __tablename__: str
    id: Any
    conn_id: Any
    conn_type: Any
    host: Any
    schema: Any
    login: Any
    port: Any
    is_encrypted: Any
    is_extra_encrypted: Any
    def __init__(self, conn_id: Any | None = ..., conn_type: Any | None = ..., host: Any | None = ..., login: Any | None = ..., password: Any | None = ..., schema: Any | None = ..., port: Any | None = ..., extra: Any | None = ..., uri: Any | None = ...) -> None: ...
    def parse_from_uri(self, uri) -> None: ...
    def get_uri(self): ...
    def get_password(self): ...
    def set_password(self, value) -> None: ...
    def password(cls): ...
    def get_extra(self): ...
    def set_extra(self, value) -> None: ...
    def extra(cls): ...
    def rotate_fernet_key(self) -> None: ...
    def get_hook(self): ...
    def log_info(self): ...
    def debug_info(self): ...
    @property
    def extra_dejson(self): ...
