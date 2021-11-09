from airflow.configuration import conf as conf
from airflow.models import Connection as Connection
from airflow.utils import timezone as timezone
from airflow.www_rbac.validators import ValidJson as ValidJson
from airflow.www_rbac.widgets import AirflowDateTimePickerWidget as AirflowDateTimePickerWidget
from flask_appbuilder.forms import DynamicForm
from flask_wtf import FlaskForm
from typing import Any
from wtforms.fields import Field

class DateTimeWithTimezoneField(Field):
    widget: Any
    format: Any
    def __init__(self, label: Any | None = ..., validators: Any | None = ..., format: Any | None = ..., **kwargs) -> None: ...
    data: Any
    def process_formdata(self, valuelist) -> None: ...

class DateTimeForm(FlaskForm):
    execution_date: Any

class DateTimeWithNumRunsForm(FlaskForm):
    base_date: Any
    num_runs: Any

class DateTimeWithNumRunsWithDagRunsForm(DateTimeWithNumRunsForm):
    execution_date: Any

class DagRunForm(DynamicForm):
    dag_id: Any
    start_date: Any
    end_date: Any
    run_id: Any
    state: Any
    execution_date: Any
    external_trigger: Any
    conf: Any
    def populate_obj(self, item) -> None: ...

class ConnectionForm(DynamicForm):
    conn_id: Any
    conn_type: Any
    host: Any
    schema: Any
    login: Any
    password: Any
    port: Any
    extra: Any
    extra__jdbc__drv_path: Any
    extra__jdbc__drv_clsname: Any
    extra__google_cloud_platform__project: Any
    extra__google_cloud_platform__key_path: Any
    extra__google_cloud_platform__keyfile_dict: Any
    extra__google_cloud_platform__scope: Any
    extra__google_cloud_platform__num_retries: Any
    extra__grpc__auth_type: Any
    extra__grpc__credential_pem_file: Any
    extra__grpc__scopes: Any
