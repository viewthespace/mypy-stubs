from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.base_hook import BaseHook as BaseHook
from typing import Any

class SqoopHook(BaseHook):
    conn: Any
    job_tracker: Any
    namenode: Any
    libjars: Any
    files: Any
    archives: Any
    password_file: Any
    hcatalog_database: Any
    hcatalog_table: Any
    verbose: Any
    num_mappers: Any
    properties: Any
    def __init__(self, conn_id: str = ..., verbose: bool = ..., num_mappers: Any | None = ..., hcatalog_database: Any | None = ..., hcatalog_table: Any | None = ..., properties: Any | None = ...) -> None: ...
    def get_conn(self): ...
    def cmd_mask_password(self, cmd_orig): ...
    sp: Any
    def Popen(self, cmd, **kwargs) -> None: ...
    def import_table(self, table, target_dir: Any | None = ..., append: bool = ..., file_type: str = ..., columns: Any | None = ..., split_by: Any | None = ..., where: Any | None = ..., direct: bool = ..., driver: Any | None = ..., extra_import_options: Any | None = ...) -> None: ...
    def import_query(self, query, target_dir, append: bool = ..., file_type: str = ..., split_by: Any | None = ..., direct: Any | None = ..., driver: Any | None = ..., extra_import_options: Any | None = ...) -> None: ...
    def export_table(self, table, export_dir, input_null_string, input_null_non_string, staging_table, clear_staging_table, enclosed_by, escaped_by, input_fields_terminated_by, input_lines_terminated_by, input_optionally_enclosed_by, batch, relaxed_isolation, extra_export_options: Any | None = ...) -> None: ...
