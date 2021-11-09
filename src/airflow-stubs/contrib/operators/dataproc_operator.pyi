from airflow.contrib.hooks.gcp_dataproc_hook import DataProcHook as DataProcHook
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils import timezone as timezone
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.version import version as version
from typing import Any

class DataprocOperationBaseOperator(BaseOperator):
    gcp_conn_id: Any
    delegate_to: Any
    project_id: Any
    region: Any
    hook: Any
    def __init__(self, project_id, region: str = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
    def start(self, context) -> None: ...

class DataprocClusterCreateOperator(DataprocOperationBaseOperator):
    template_fields: Any
    cluster_name: Any
    num_masters: Any
    num_workers: Any
    num_preemptible_workers: Any
    storage_bucket: Any
    init_actions_uris: Any
    init_action_timeout: Any
    metadata: Any
    custom_image: Any
    custom_image_project_id: Any
    image_version: Any
    properties: Any
    optional_components: Any
    master_machine_type: Any
    master_disk_type: Any
    master_disk_size: Any
    autoscaling_policy: Any
    worker_machine_type: Any
    worker_disk_type: Any
    worker_disk_size: Any
    labels: Any
    zone: Any
    network_uri: Any
    subnetwork_uri: Any
    internal_ip_only: Any
    tags: Any
    service_account: Any
    service_account_scopes: Any
    idle_delete_ttl: Any
    auto_delete_time: Any
    auto_delete_ttl: Any
    customer_managed_key: Any
    single_node: Any
    def __init__(self, project_id, cluster_name, num_workers, zone: Any | None = ..., network_uri: Any | None = ..., subnetwork_uri: Any | None = ..., internal_ip_only: Any | None = ..., tags: Any | None = ..., storage_bucket: Any | None = ..., init_actions_uris: Any | None = ..., init_action_timeout: str = ..., metadata: Any | None = ..., custom_image: Any | None = ..., custom_image_project_id: Any | None = ..., image_version: Any | None = ..., autoscaling_policy: Any | None = ..., properties: Any | None = ..., optional_components: Any | None = ..., num_masters: int = ..., master_machine_type: str = ..., master_disk_type: str = ..., master_disk_size: int = ..., worker_machine_type: str = ..., worker_disk_type: str = ..., worker_disk_size: int = ..., num_preemptible_workers: int = ..., labels: Any | None = ..., region: str = ..., service_account: Any | None = ..., service_account_scopes: Any | None = ..., idle_delete_ttl: Any | None = ..., auto_delete_time: Any | None = ..., auto_delete_ttl: Any | None = ..., customer_managed_key: Any | None = ..., *args, **kwargs) -> None: ...
    def start(self): ...

class DataprocClusterScaleOperator(DataprocOperationBaseOperator):
    template_fields: Any
    cluster_name: Any
    num_workers: Any
    num_preemptible_workers: Any
    optional_arguments: Any
    def __init__(self, cluster_name, project_id, region: str = ..., num_workers: int = ..., num_preemptible_workers: int = ..., graceful_decommission_timeout: Any | None = ..., *args, **kwargs) -> None: ...
    def start(self): ...

class DataprocClusterDeleteOperator(DataprocOperationBaseOperator):
    template_fields: Any
    cluster_name: Any
    def __init__(self, cluster_name, project_id, region: str = ..., *args, **kwargs) -> None: ...
    def start(self): ...

class DataProcJobBaseOperator(BaseOperator):
    job_type: str
    gcp_conn_id: Any
    delegate_to: Any
    labels: Any
    job_name: Any
    cluster_name: Any
    dataproc_properties: Any
    dataproc_jars: Any
    region: Any
    job_error_states: Any
    hook: Any
    job_template: Any
    job: Any
    dataproc_job_id: Any
    def __init__(self, job_name: str = ..., cluster_name: str = ..., dataproc_properties: Any | None = ..., dataproc_jars: Any | None = ..., gcp_conn_id: str = ..., delegate_to: Any | None = ..., labels: Any | None = ..., region: str = ..., job_error_states: Any | None = ..., *args, **kwargs) -> None: ...
    def create_job_template(self) -> None: ...
    def execute(self, context) -> None: ...
    def on_kill(self) -> None: ...

class DataProcPigOperator(DataProcJobBaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    job_type: str
    query: Any
    query_uri: Any
    variables: Any
    def __init__(self, query: Any | None = ..., query_uri: Any | None = ..., variables: Any | None = ..., dataproc_pig_properties: Any | None = ..., dataproc_pig_jars: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class DataProcHiveOperator(DataProcJobBaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    job_type: str
    query: Any
    query_uri: Any
    variables: Any
    def __init__(self, query: Any | None = ..., query_uri: Any | None = ..., variables: Any | None = ..., dataproc_hive_properties: Any | None = ..., dataproc_hive_jars: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class DataProcSparkSqlOperator(DataProcJobBaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    job_type: str
    query: Any
    query_uri: Any
    variables: Any
    def __init__(self, query: Any | None = ..., query_uri: Any | None = ..., variables: Any | None = ..., dataproc_spark_properties: Any | None = ..., dataproc_spark_jars: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class DataProcSparkOperator(DataProcJobBaseOperator):
    template_fields: Any
    ui_color: str
    job_type: str
    main_jar: Any
    main_class: Any
    arguments: Any
    archives: Any
    files: Any
    def __init__(self, main_jar: Any | None = ..., main_class: Any | None = ..., arguments: Any | None = ..., archives: Any | None = ..., files: Any | None = ..., dataproc_spark_properties: Any | None = ..., dataproc_spark_jars: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class DataProcHadoopOperator(DataProcJobBaseOperator):
    template_fields: Any
    ui_color: str
    job_type: str
    main_jar: Any
    main_class: Any
    arguments: Any
    archives: Any
    files: Any
    def __init__(self, main_jar: Any | None = ..., main_class: Any | None = ..., arguments: Any | None = ..., archives: Any | None = ..., files: Any | None = ..., dataproc_hadoop_properties: Any | None = ..., dataproc_hadoop_jars: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class DataProcPySparkOperator(DataProcJobBaseOperator):
    template_fields: Any
    ui_color: str
    job_type: str
    main: Any
    arguments: Any
    archives: Any
    files: Any
    pyfiles: Any
    def __init__(self, main, arguments: Any | None = ..., archives: Any | None = ..., pyfiles: Any | None = ..., files: Any | None = ..., dataproc_pyspark_properties: Any | None = ..., dataproc_pyspark_jars: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...

class DataprocWorkflowTemplateInstantiateOperator(DataprocOperationBaseOperator):
    template_fields: Any
    template_id: Any
    def __init__(self, template_id, *args, **kwargs) -> None: ...
    def start(self): ...

class DataprocWorkflowTemplateInstantiateInlineOperator(DataprocOperationBaseOperator):
    template_fields: Any
    template: Any
    def __init__(self, template, *args, **kwargs) -> None: ...
    def start(self): ...
