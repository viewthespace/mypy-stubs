from airflow.contrib.hooks.sqoop_hook import SqoopHook as SqoopHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class SqoopOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    conn_id: Any
    cmd_type: Any
    table: Any
    query: Any
    target_dir: Any
    append: Any
    file_type: Any
    columns: Any
    num_mappers: Any
    split_by: Any
    where: Any
    export_dir: Any
    input_null_string: Any
    input_null_non_string: Any
    staging_table: Any
    clear_staging_table: Any
    enclosed_by: Any
    escaped_by: Any
    input_fields_terminated_by: Any
    input_lines_terminated_by: Any
    input_optionally_enclosed_by: Any
    batch: Any
    direct: Any
    driver: Any
    verbose: Any
    relaxed_isolation: Any
    hcatalog_database: Any
    hcatalog_table: Any
    create_hcatalog_table: Any
    properties: Any
    extra_import_options: Any
    extra_export_options: Any
    def __init__(self, conn_id: str = ..., cmd_type: str = ..., table: Any | None = ..., query: Any | None = ..., target_dir: Any | None = ..., append: Any | None = ..., file_type: str = ..., columns: Any | None = ..., num_mappers: Any | None = ..., split_by: Any | None = ..., where: Any | None = ..., export_dir: Any | None = ..., input_null_string: Any | None = ..., input_null_non_string: Any | None = ..., staging_table: Any | None = ..., clear_staging_table: bool = ..., enclosed_by: Any | None = ..., escaped_by: Any | None = ..., input_fields_terminated_by: Any | None = ..., input_lines_terminated_by: Any | None = ..., input_optionally_enclosed_by: Any | None = ..., batch: bool = ..., direct: bool = ..., driver: Any | None = ..., verbose: bool = ..., relaxed_isolation: bool = ..., properties: Any | None = ..., hcatalog_database: Any | None = ..., hcatalog_table: Any | None = ..., create_hcatalog_table: bool = ..., extra_import_options: Any | None = ..., extra_export_options: Any | None = ..., *args, **kwargs) -> None: ...
    hook: Any
    def execute(self, context) -> None: ...
    def on_kill(self) -> None: ...
