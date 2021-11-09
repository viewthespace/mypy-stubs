import inspect
from airflow import settings as settings
from airflow.exceptions import AirflowException as AirflowException
from typing import Any, Callable, TypeVar

PY2: bool
signature = inspect.signature

F = TypeVar('F', bound=Callable[..., Any])

def apply_defaults(func: F) -> F: ...
