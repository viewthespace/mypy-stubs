from airflow.configuration import conf as conf, mkdir_p as mkdir_p
from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.utils.state import State as State
from typing import Any

log: Any
COMMAND_CLASSES: Any
POSITIONAL_ARGS: Any

def flatten_list(list_of_lists): ...
def filter_options(options): ...
def get_options_list(command_class): ...
def build_command_args(): ...

COMMAND_ARGS: Any
HYPHEN_ARGS: Any

class QuboleHook(BaseHook):
    task_id: Any
    dag_id: Any
    kwargs: Any
    cls: Any
    cmd: Any
    task_instance: Any
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def handle_failure_retry(context) -> None: ...
    def execute(self, context) -> None: ...
    def kill(self, ti) -> None: ...
    def get_results(self, ti: Any | None = ..., fp: Any | None = ..., inline: bool = ..., delim: Any | None = ..., fetch: bool = ...): ...
    def get_log(self, ti) -> None: ...
    def get_jobs_id(self, ti) -> None: ...
    def create_cmd_args(self, context): ...