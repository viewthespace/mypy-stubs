from airflow.hooks.druid_hook import DruidHook as DruidHook
from airflow.hooks.hive_hooks import HiveCliHook as HiveCliHook, HiveMetastoreHook as HiveMetastoreHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

LOAD_CHECK_INTERVAL: int
DEFAULT_TARGET_PARTITION_SIZE: int

class HiveToDruidTransfer(BaseOperator):
    template_fields: Any
    template_ext: Any
    sql: Any
    druid_datasource: Any
    ts_dim: Any
    intervals: Any
    num_shards: Any
    target_partition_size: Any
    query_granularity: Any
    segment_granularity: Any
    metric_spec: Any
    hive_cli_conn_id: Any
    hadoop_dependency_coordinates: Any
    druid_ingest_conn_id: Any
    metastore_conn_id: Any
    hive_tblproperties: Any
    job_properties: Any
    def __init__(self, sql, druid_datasource, ts_dim, metric_spec: Any | None = ..., hive_cli_conn_id: str = ..., druid_ingest_conn_id: str = ..., metastore_conn_id: str = ..., hadoop_dependency_coordinates: Any | None = ..., intervals: Any | None = ..., num_shards: int = ..., target_partition_size: int = ..., query_granularity: str = ..., segment_granularity: str = ..., hive_tblproperties: Any | None = ..., job_properties: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
    def construct_ingest_query(self, static_path, columns): ...
