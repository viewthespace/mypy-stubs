from airflow import models as models
from airflow.contrib.operators.gcp_bigtable_operator import BigtableClusterUpdateOperator as BigtableClusterUpdateOperator, BigtableInstanceCreateOperator as BigtableInstanceCreateOperator, BigtableInstanceDeleteOperator as BigtableInstanceDeleteOperator, BigtableTableCreateOperator as BigtableTableCreateOperator, BigtableTableDeleteOperator as BigtableTableDeleteOperator, BigtableTableWaitForReplicationSensor as BigtableTableWaitForReplicationSensor
from airflow.utils.dates import days_ago as days_ago
from typing import Any

GCP_PROJECT_ID: Any
CBT_INSTANCE_ID: Any
CBT_INSTANCE_DISPLAY_NAME: Any
CBT_INSTANCE_TYPE: Any
CBT_INSTANCE_LABELS: Any
CBT_CLUSTER_ID: Any
CBT_CLUSTER_ZONE: Any
CBT_CLUSTER_NODES: Any
CBT_CLUSTER_NODES_UPDATED: Any
CBT_CLUSTER_STORAGE_TYPE: Any
CBT_TABLE_ID: Any
CBT_POKE_INTERVAL: Any
default_args: Any
create_instance_task: Any
create_instance_task2: Any
cluster_update_task: Any
cluster_update_task2: Any
delete_instance_task: Any
delete_instance_task2: Any
create_table_task: Any
create_table_task2: Any
wait_for_table_replication_task: Any
wait_for_table_replication_task2: Any
delete_table_task: Any
delete_table_task2: Any
