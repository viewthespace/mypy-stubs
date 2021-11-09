from airflow.contrib.hooks.bigquery_hook import BigQueryHook as BigQueryHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models.baseoperator import BaseOperator as BaseOperator, BaseOperatorLink as BaseOperatorLink
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

BIGQUERY_JOB_DETAILS_LINK_FMT: str

class BigQueryConsoleLink(BaseOperatorLink):
    name: str
    def get_link(self, operator, dttm): ...

class BigQueryConsoleIndexableLink(BaseOperatorLink):
    index: Any
    def __init__(self, index) -> None: ...
    @property
    def name(self) -> str: ...
    def get_link(self, operator, dttm): ...

class BigQueryOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    @property
    def operator_extra_links(self): ...
    bql: Any
    sql: Any
    destination_dataset_table: Any
    write_disposition: Any
    create_disposition: Any
    allow_large_results: Any
    flatten_results: Any
    bigquery_conn_id: Any
    delegate_to: Any
    udf_config: Any
    use_legacy_sql: Any
    maximum_billing_tier: Any
    maximum_bytes_billed: Any
    schema_update_options: Any
    query_params: Any
    labels: Any
    bq_cursor: Any
    priority: Any
    time_partitioning: Any
    api_resource_configs: Any
    cluster_fields: Any
    location: Any
    encryption_configuration: Any
    def __init__(self, bql: Any | None = ..., sql: Any | None = ..., destination_dataset_table: Any | None = ..., write_disposition: str = ..., allow_large_results: bool = ..., flatten_results: Any | None = ..., bigquery_conn_id: str = ..., delegate_to: Any | None = ..., udf_config: Any | None = ..., use_legacy_sql: bool = ..., maximum_billing_tier: Any | None = ..., maximum_bytes_billed: Any | None = ..., create_disposition: str = ..., schema_update_options=..., query_params: Any | None = ..., labels: Any | None = ..., priority: str = ..., time_partitioning: Any | None = ..., api_resource_configs: Any | None = ..., cluster_fields: Any | None = ..., location: Any | None = ..., encryption_configuration: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
    def on_kill(self) -> None: ...

class BigQueryCreateEmptyTableOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    project_id: Any
    dataset_id: Any
    table_id: Any
    schema_fields: Any
    gcs_schema_object: Any
    bigquery_conn_id: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    time_partitioning: Any
    labels: Any
    encryption_configuration: Any
    def __init__(self, dataset_id, table_id, project_id: Any | None = ..., schema_fields: Any | None = ..., gcs_schema_object: Any | None = ..., time_partitioning: Any | None = ..., bigquery_conn_id: str = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., labels: Any | None = ..., encryption_configuration: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class BigQueryCreateExternalTableOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    bucket: Any
    source_objects: Any
    schema_object: Any
    destination_project_dataset_table: Any
    schema_fields: Any
    source_format: Any
    compression: Any
    skip_leading_rows: Any
    field_delimiter: Any
    max_bad_records: Any
    quote_character: Any
    allow_quoted_newlines: Any
    allow_jagged_rows: Any
    bigquery_conn_id: Any
    google_cloud_storage_conn_id: Any
    delegate_to: Any
    src_fmt_configs: Any
    labels: Any
    encryption_configuration: Any
    def __init__(self, bucket, source_objects, destination_project_dataset_table, schema_fields: Any | None = ..., schema_object: Any | None = ..., source_format: str = ..., compression: str = ..., skip_leading_rows: int = ..., field_delimiter: str = ..., max_bad_records: int = ..., quote_character: Any | None = ..., allow_quoted_newlines: bool = ..., allow_jagged_rows: bool = ..., bigquery_conn_id: str = ..., google_cloud_storage_conn_id: str = ..., delegate_to: Any | None = ..., src_fmt_configs: Any | None = ..., labels: Any | None = ..., encryption_configuration: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class BigQueryDeleteDatasetOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    dataset_id: Any
    project_id: Any
    bigquery_conn_id: Any
    delete_contents: Any
    delegate_to: Any
    def __init__(self, dataset_id, delete_contents: bool = ..., project_id: Any | None = ..., bigquery_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class BigQueryCreateEmptyDatasetOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    dataset_id: Any
    project_id: Any
    bigquery_conn_id: Any
    dataset_reference: Any
    delegate_to: Any
    def __init__(self, dataset_id, project_id: Any | None = ..., dataset_reference: Any | None = ..., bigquery_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class BigQueryGetDatasetOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    dataset_id: Any
    project_id: Any
    gcp_conn_id: Any
    delegate_to: Any
    def __init__(self, dataset_id, project_id: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class BigQueryPatchDatasetOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    dataset_id: Any
    project_id: Any
    gcp_conn_id: Any
    dataset_resource: Any
    delegate_to: Any
    def __init__(self, dataset_id, dataset_resource, project_id: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...

class BigQueryUpdateDatasetOperator(BaseOperator):
    template_fields: Any
    ui_color: str
    dataset_id: Any
    project_id: Any
    gcp_conn_id: Any
    dataset_resource: Any
    delegate_to: Any
    def __init__(self, dataset_id, dataset_resource, project_id: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
