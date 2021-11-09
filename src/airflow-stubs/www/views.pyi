from airflow import configuration as configuration, jobs as jobs, models as models, settings as settings
from airflow.api.common.experimental.mark_tasks import set_dag_run_state_to_failed as set_dag_run_state_to_failed, set_dag_run_state_to_running as set_dag_run_state_to_running, set_dag_run_state_to_success as set_dag_run_state_to_success
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator, Connection as Connection, DagRun as DagRun, XCom as XCom, errors as errors
from airflow.models.dagcode import DagCode as DagCode
from airflow.operators.subdag_operator import SubDagOperator as SubDagOperator
from airflow.settings import STATE_COLORS as STATE_COLORS, STORE_SERIALIZED_DAGS as STORE_SERIALIZED_DAGS
from airflow.ti_deps.dep_context import DepContext as DepContext, RUNNING_DEPS as RUNNING_DEPS, SCHEDULER_QUEUED_DEPS as SCHEDULER_QUEUED_DEPS
from airflow.utils import timezone as timezone
from airflow.utils.dates import infer_time_unit as infer_time_unit, parse_execution_date as parse_execution_date, scale_time_units as scale_time_units
from airflow.utils.db import create_session as create_session, provide_session as provide_session
from airflow.utils.helpers import alchemy_to_dict as alchemy_to_dict, render_log_filename as render_log_filename
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.state import State as State
from airflow.utils.timezone import datetime as datetime
from airflow.www import utils as wwwutils
from airflow.www.forms import DateTimeForm as DateTimeForm, DateTimeWithNumRunsForm as DateTimeWithNumRunsForm, DateTimeWithNumRunsWithDagRunsForm as DateTimeWithNumRunsWithDagRunsForm
from airflow.www.utils import wrapped_markdown as wrapped_markdown
from airflow.www.validators import GreaterEqualThan as GreaterEqualThan
from flask_admin import AdminIndexView, BaseView
from flask_admin.contrib.sqla import ModelView
from typing import Any

QUERY_LIMIT: int
CHART_LIMIT: int
UTF8_READER: Any
dagbag: Any
login_required: Any
current_user: Any
logout_user: Any
FILTER_BY_OWNER: bool
PAGE_SIZE: Any
log: Any

def dag_link(v, c, m, p): ...
def log_url_formatter(v, c, m, p): ...
def dag_run_link(v, c, m, p): ...
def task_instance_link(v, c, m, p): ...
def state_token(state): ...
def parse_datetime_f(value): ...
def state_f(v, c, m, p): ...
def duration_f(v, c, m, p): ...
def datetime_f(v, c, m, p): ...
def nobr_f(v, c, m, p): ...
def label_link(v, c, m, p): ...
def pool_link(v, c, m, p): ...
def pygment_html_render(s, lexer=...): ...
def render(obj, lexer): ...

attr_renderer: Any

def data_profiling_required(f): ...
def fused_slots(v, c, m, p): ...
def fqueued_slots(v, c, m, p): ...
def recurse_tasks(tasks, task_ids, dag_ids, task_id_to_dag) -> None: ...
def get_chart_height(dag): ...
def get_safe_url(url): ...
def get_date_time_num_runs_dag_runs_form_data(request, session, dag): ...

class AirflowViewMixin:
    def render(self, template, **kwargs): ...

class Airflow(AirflowViewMixin, BaseView):
    def is_visible(self): ...
    def index(self): ...
    def chart_data(self): ...
    def chart(self): ...
    def dag_stats(self, session: Any | None = ...): ...
    def task_stats(self, session: Any | None = ...): ...
    def code(self, session: Any | None = ...): ...
    def dag_details(self, session: Any | None = ...): ...
    def circles(self): ...
    def show_traceback(self): ...
    def noaccess(self): ...
    def pickle_info(self): ...
    def login(self): ...
    def logout(self): ...
    def rendered(self, session: Any | None = ...): ...
    def get_logs_with_metadata(self, session: Any | None = ...): ...
    def log(self, session: Any | None = ...): ...
    def elasticsearch(self, session: Any | None = ...): ...
    def task(self): ...
    def xcom(self, session: Any | None = ...): ...
    def run(self): ...
    def delete(self): ...
    def trigger(self, session: Any | None = ...): ...
    def clear(self): ...
    def dagrun_clear(self): ...
    def blocked(self, session: Any | None = ...): ...
    def dagrun_failed(self): ...
    def dagrun_success(self): ...
    def failed(self): ...
    def success(self): ...
    def tree(self, session: Any | None = ...): ...
    def graph(self, session: Any | None = ...): ...
    def duration(self, session: Any | None = ...): ...
    def tries(self, session: Any | None = ...): ...
    def landing_times(self, session: Any | None = ...): ...
    def paused(self, session: Any | None = ...): ...
    def refresh(self, session: Any | None = ...): ...
    def gantt(self, session: Any | None = ...): ...
    def task_instances(self, session: Any | None = ...): ...
    def variables(self, form): ...
    def varimport(self): ...

class HomeView(AirflowViewMixin, AdminIndexView):
    def index(self, session: Any | None = ...): ...

class QueryView(wwwutils.DataProfilingMixin, AirflowViewMixin, BaseView):
    def query(self, session: Any | None = ...): ...

class AirflowModelView(AirflowViewMixin, ModelView):
    list_template: str
    edit_template: str
    create_template: str
    column_display_actions: bool
    page_size: Any

class ModelViewOnly(wwwutils.LoginMixin, AirflowModelView):
    named_filter_urls: bool
    can_create: bool
    can_edit: bool
    can_delete: bool
    column_display_pk: bool

class PoolModelView(wwwutils.SuperUserMixin, AirflowModelView):
    column_list: Any
    column_formatters: Any
    named_filter_urls: bool
    validators_columns: Any
    form_args: Any
    def delete_model(self, model): ...

class SlaMissModelView(wwwutils.SuperUserMixin, ModelViewOnly):
    verbose_name_plural: str
    verbose_name: str
    column_list: Any
    column_formatters: Any
    named_filter_urls: bool
    column_searchable_list: Any
    column_filters: Any
    filter_converter: Any
    form_widget_args: Any

class ChartModelView(wwwutils.DataProfilingMixin, AirflowModelView):
    verbose_name: str
    verbose_name_plural: str
    form_columns: Any
    column_list: Any
    column_sortable_list: Any
    column_formatters: Any
    column_default_sort: Any
    create_template: str
    edit_template: str
    column_filters: Any
    column_searchable_list: Any
    column_descriptions: Any
    column_labels: Any
    form_choices: Any
    def on_model_change(self, form, model, is_created: bool = ...) -> None: ...

chart_mapping: Any

class KnownEventView(wwwutils.DataProfilingMixin, AirflowModelView):
    verbose_name: str
    verbose_name_plural: str
    form_columns: Any
    form_args: Any
    column_list: Any
    column_default_sort: Any
    column_sortable_list: Any
    filter_converter: Any
    form_overrides: Any

class KnownEventTypeView(wwwutils.DataProfilingMixin, AirflowModelView): ...

class VariableView(wwwutils.DataProfilingMixin, AirflowModelView):
    verbose_name: str
    verbose_name_plural: str
    list_template: str
    def hidden_field_formatter(view, context, model, name): ...
    form_columns: Any
    column_list: Any
    column_filters: Any
    column_searchable_list: Any
    column_default_sort: Any
    form_widget_args: Any
    form_args: Any
    column_sortable_list: Any
    column_formatters: Any
    def action_varexport(self, ids, session: Any | None = ...): ...
    def on_form_prefill(self, form, id) -> None: ...

class XComView(wwwutils.SuperUserMixin, AirflowModelView):
    can_create: bool
    can_edit: bool
    verbose_name: str
    verbose_name_plural: str
    form_columns: Any
    form_extra_fields: Any
    form_args: Any
    column_filters: Any
    column_searchable_list: Any
    filter_converter: Any
    form_overrides: Any
    def on_model_change(self, form, model, is_created) -> None: ...

class JobModelView(ModelViewOnly):
    verbose_name_plural: str
    verbose_name: str
    column_display_actions: bool
    column_default_sort: Any
    column_filters: Any
    column_formatters: Any
    filter_converter: Any

class DagRunModelView(ModelViewOnly):
    verbose_name_plural: str
    can_edit: bool
    can_create: bool
    verbose_name: str
    column_default_sort: Any
    form_choices: Any
    form_args: Any
    column_list: Any
    column_filters: Any
    filter_converter: Any
    column_searchable_list: Any
    column_formatters: Any
    form_overrides: Any
    def action_new_delete(self, ids, session: Any | None = ...) -> None: ...
    def action_set_running(self, ids, session: Any | None = ...) -> None: ...
    def action_set_failed(self, ids, session: Any | None = ...) -> None: ...
    def action_set_success(self, ids, session: Any | None = ...) -> None: ...
    def after_model_change(self, form, dagrun, is_created, session: Any | None = ...) -> None: ...

class LogModelView(ModelViewOnly):
    verbose_name_plural: str
    verbose_name: str
    column_display_actions: bool
    column_default_sort: Any
    column_filters: Any
    filter_converter: Any
    column_formatters: Any

class TaskInstanceModelView(ModelViewOnly):
    verbose_name_plural: str
    verbose_name: str
    column_filters: Any
    filter_converter: Any
    named_filter_urls: bool
    column_formatters: Any
    column_searchable_list: Any
    column_default_sort: Any
    form_choices: Any
    column_list: Any
    page_size: Any
    def action_set_running(self, ids) -> None: ...
    def action_set_failed(self, ids) -> None: ...
    def action_set_success(self, ids) -> None: ...
    def action_set_retry(self, ids) -> None: ...
    def action_clear(self, ids, session: Any | None = ...) -> None: ...
    def set_task_instance_state(self, ids, target_state, session: Any | None = ...) -> None: ...
    def get_one(self, id): ...

class ConnectionModelView(wwwutils.SuperUserMixin, AirflowModelView):
    create_template: str
    edit_template: str
    list_template: str
    form_columns: Any
    verbose_name: str
    verbose_name_plural: str
    column_default_sort: Any
    column_list: Any
    form_overrides: Any
    form_args: Any
    form_widget_args: Any
    form_extra_fields: Any
    form_choices: Any
    def on_model_change(self, form, model, is_created) -> None: ...
    @classmethod
    def alert_fernet_key(cls): ...
    @classmethod
    def is_secure(cls): ...
    def on_form_prefill(self, form, id) -> None: ...

class UserModelView(wwwutils.SuperUserMixin, AirflowModelView):
    verbose_name: str
    verbose_name_plural: str
    column_default_sort: str

class VersionView(wwwutils.SuperUserMixin, AirflowViewMixin, BaseView):
    def version(self): ...

class ConfigurationView(wwwutils.SuperUserMixin, AirflowViewMixin, BaseView):
    def conf(self): ...

class DagModelView(wwwutils.SuperUserMixin, ModelView):
    column_list: Any
    column_editable_list: Any
    form_excluded_columns: Any
    column_searchable_list: Any
    column_filters: Any
    filter_converter: Any
    form_widget_args: Any
    column_formatters: Any
    can_delete: bool
    can_create: bool
    page_size: Any
    list_template: str
    named_filter_urls: bool
    def get_query(self): ...
    def get_count_query(self): ...
    def edit_form(self, obj: Any | None = ...): ...
