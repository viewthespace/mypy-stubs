from airflow.exceptions import AirflowException as AirflowException, AirflowFileParseException as AirflowFileParseException, file_syntax_error as file_syntax_error
from airflow.secrets.base_secrets import BaseSecretsBackend as BaseSecretsBackend
from airflow.utils.file import COMMENT_PATTERN as COMMENT_PATTERN
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

log: Any

def get_connection_parameter_names(): ...

FILE_PARSERS: Any

def load_variables(file_path): ...
def load_connections(file_path): ...

class LocalFilesystemBackend(BaseSecretsBackend, LoggingMixin):
    variables_file: Any
    connections_file: Any
    def __init__(self, variables_file_path: Any | None = ..., connections_file_path: Any | None = ...) -> None: ...
    def get_connections(self, conn_id): ...
    def get_variable(self, key): ...
