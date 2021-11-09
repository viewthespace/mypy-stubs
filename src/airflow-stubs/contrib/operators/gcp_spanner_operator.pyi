from airflow import AirflowException as AirflowException
from airflow.contrib.hooks.gcp_spanner_hook import CloudSpannerHook as CloudSpannerHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class CloudSpannerInstanceDeployOperator(BaseOperator):
    template_fields: Any
    instance_id: Any
    project_id: Any
    configuration_name: Any
    node_count: Any
    display_name: Any
    gcp_conn_id: Any
    def __init__(self, instance_id, configuration_name, node_count, display_name, project_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class CloudSpannerInstanceDeleteOperator(BaseOperator):
    template_fields: Any
    instance_id: Any
    project_id: Any
    gcp_conn_id: Any
    def __init__(self, instance_id, project_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSpannerInstanceDatabaseQueryOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    instance_id: Any
    project_id: Any
    database_id: Any
    query: Any
    gcp_conn_id: Any
    def __init__(self, instance_id, database_id, query, project_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
    @staticmethod
    def sanitize_queries(queries) -> None: ...

class CloudSpannerInstanceDatabaseDeployOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    instance_id: Any
    project_id: Any
    database_id: Any
    ddl_statements: Any
    gcp_conn_id: Any
    def __init__(self, instance_id, database_id, ddl_statements, project_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSpannerInstanceDatabaseUpdateOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    instance_id: Any
    project_id: Any
    database_id: Any
    ddl_statements: Any
    operation_id: Any
    gcp_conn_id: Any
    def __init__(self, instance_id, database_id, ddl_statements, project_id: Any | None = ..., operation_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class CloudSpannerInstanceDatabaseDeleteOperator(BaseOperator):
    template_fields: Any
    instance_id: Any
    project_id: Any
    database_id: Any
    gcp_conn_id: Any
    def __init__(self, instance_id, database_id, project_id: Any | None = ..., gcp_conn_id: str = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
