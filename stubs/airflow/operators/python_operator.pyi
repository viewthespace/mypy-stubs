from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator, SkipMixin as SkipMixin
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.file import TemporaryDirectory as TemporaryDirectory
from airflow.utils.operator_helpers import context_to_airflow_vars as context_to_airflow_vars
from builtins import str
from typing import Any, Callable, Dict, Iterable, Optional

class PythonOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    shallow_copy_attrs: Any
    python_callable: Any
    op_args: Any
    op_kwargs: Any
    provide_context: Any
    templates_dict: Any
    template_ext: Any
    def __init__(self, python_callable: Callable, op_args: Optional[Iterable] = ..., op_kwargs: Optional[Dict] = ..., provide_context: bool = ..., templates_dict: Optional[Dict] = ..., templates_exts: Optional[Iterable[str]] = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
    def execute_callable(self): ...

class BranchPythonOperator(PythonOperator, SkipMixin):
    def execute(self, context) -> None: ...

class ShortCircuitOperator(PythonOperator, SkipMixin):
    def execute(self, context) -> None: ...

class PythonVirtualenvOperator(PythonOperator):
    requirements: Any
    string_args: Any
    python_version: Any
    use_dill: Any
    system_site_packages: Any
    def __init__(self, python_callable: Callable, requirements: Optional[Iterable[str]] = ..., python_version: Optional[str] = ..., use_dill: bool = ..., system_site_packages: bool = ..., op_args: Optional[Iterable] = ..., op_kwargs: Optional[Dict] = ..., provide_context: bool = ..., string_args: Optional[Iterable[str]] = ..., templates_dict: Optional[Dict] = ..., templates_exts: Optional[Iterable[str]] = ..., *args, **kwargs): ...
    def execute_callable(self): ...
