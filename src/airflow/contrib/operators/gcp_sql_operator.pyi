from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_sql_hook import CloudSqlDatabaseHook as CloudSqlDatabaseHook, CloudSqlHook as CloudSqlHook
from airflow.contrib.utils.gcp_field_validator import GcpBodyFieldValidator as GcpBodyFieldValidator
from airflow.hooks.base_hook import BaseHook as BaseHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

SETTINGS: str
SETTINGS_VERSION: str
CLOUD_SQL_CREATE_VALIDATION: Any
CLOUD_SQL_EXPORT_VALIDATION: Any
CLOUD_SQL_IMPORT_VALIDATION: Any
CLOUD_SQL_DATABASE_CREATE_VALIDATION: Any
CLOUD_SQL_DATABASE_PATCH_VALIDATION: Any

class CloudSqlBaseOperator(BaseOperator):
    project_id: Any
    instance: Any
    gcp_conn_id: Any
    api_version: Any
    def __init__(self, instance, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudSqlInstanceCreateOperator(CloudSqlBaseOperator):
    template_fields: Any
    body: Any
    validate_body: Any
    def __init__(self, body, instance, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., validate_body: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudSqlInstancePatchOperator(CloudSqlBaseOperator):
    template_fields: Any
    body: Any
    def __init__(self, body, instance, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSqlInstanceDeleteOperator(CloudSqlBaseOperator):
    template_fields: Any
    def __init__(self, instance, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSqlInstanceDatabaseCreateOperator(CloudSqlBaseOperator):
    template_fields: Any
    body: Any
    validate_body: Any
    def __init__(self, instance, body, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., validate_body: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSqlInstanceDatabasePatchOperator(CloudSqlBaseOperator):
    template_fields: Any
    database: Any
    body: Any
    validate_body: Any
    def __init__(self, instance, database, body, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., validate_body: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSqlInstanceDatabaseDeleteOperator(CloudSqlBaseOperator):
    template_fields: Any
    database: Any
    def __init__(self, instance, database, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSqlInstanceExportOperator(CloudSqlBaseOperator):
    template_fields: Any
    body: Any
    validate_body: Any
    def __init__(self, instance, body, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., validate_body: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSqlInstanceImportOperator(CloudSqlBaseOperator):
    template_fields: Any
    body: Any
    validate_body: Any
    def __init__(self, instance, body, project_id: Any | None = ..., gcp_conn_id: str = ..., api_version: str = ..., validate_body: bool = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSqlQueryOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    sql: Any
    gcp_conn_id: Any
    gcp_cloudsql_conn_id: Any
    autocommit: Any
    parameters: Any
    gcp_connection: Any
    cloudsql_db_hook: Any
    cloud_sql_proxy_runner: Any
    database_hook: Any
    def __init__(self, sql, autocommit: bool = ..., parameters: Any | None = ..., gcp_conn_id: str = ..., gcp_cloudsql_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
