import flask_appbuilder.models.sqla.filters as fab_sqlafilters
from airflow.configuration import conf as conf
from airflow.models import BaseOperator as BaseOperator
from airflow.operators.subdag_operator import SubDagOperator as SubDagOperator
from airflow.utils import timezone as timezone
from airflow.utils.json import AirflowJsonEncoder as AirflowJsonEncoder
from airflow.utils.state import State as State
from airflow.www_rbac.forms import DateTimeWithTimezoneField as DateTimeWithTimezoneField
from airflow.www_rbac.widgets import AirflowDateTimePickerWidget as AirflowDateTimePickerWidget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from typing import Any

AUTHENTICATE: Any
DEFAULT_SENSITIVE_VARIABLE_FIELDS: Any

def should_hide_value_for_key(key_name): ...
def get_params(**kwargs): ...
def generate_pages(current_page, num_of_pages, search: Any | None = ..., status: Any | None = ..., window: int = ...): ...
def epoch(dttm): ...
def json_response(obj): ...
def make_cache_key(*args, **kwargs): ...
def task_instance_link(attr): ...
def state_token(state): ...
def state_f(attr): ...
def nobr_f(attr_name): ...
def datetime_f(attr_name): ...
def dag_link(attr): ...
def dag_run_link(attr): ...
def pygment_html_render(s, lexer=...): ...
def render(obj, lexer): ...
def wrapped_markdown(s, css_class: Any | None = ...): ...
def get_attr_renderer(): ...
def recurse_tasks(tasks, task_ids, dag_ids, task_id_to_dag) -> None: ...
def get_chart_height(dag): ...
def get_python_source(x, return_none_if_x_none: bool = ...): ...

class UtcAwareFilterMixin:
    def apply(self, query, value): ...

class UtcAwareFilterEqual(UtcAwareFilterMixin, fab_sqlafilters.FilterEqual): ...
class UtcAwareFilterGreater(UtcAwareFilterMixin, fab_sqlafilters.FilterGreater): ...
class UtcAwareFilterSmaller(UtcAwareFilterMixin, fab_sqlafilters.FilterSmaller): ...
class UtcAwareFilterNotEqual(UtcAwareFilterMixin, fab_sqlafilters.FilterNotEqual): ...

class UtcAwareFilterConverter(fab_sqlafilters.SQLAFilterConverter):
    conversion_table: Any

class CustomSQLAInterface(SQLAInterface):
    list_properties: Any
    list_columns: Any
    def __init__(self, obj, session: Any | None = ...) -> None: ...
    def is_utcdatetime(self, col_name): ...
    filter_converter_class: Any