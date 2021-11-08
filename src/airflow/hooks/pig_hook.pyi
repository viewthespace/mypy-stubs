from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.utils.file import TemporaryDirectory as TemporaryDirectory
from typing import Any

class PigCliHook(BaseHook):
    pig_properties: Any
    conn: Any
    def __init__(self, pig_cli_conn_id: str = ...) -> None: ...
    sp: Any
    def run_cli(self, pig, pig_opts: Any | None = ..., verbose: bool = ...): ...
    def kill(self) -> None: ...
