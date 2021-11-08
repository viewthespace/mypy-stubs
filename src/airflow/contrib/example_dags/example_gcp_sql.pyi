from airflow import models as models
from airflow.contrib.operators.gcp_sql_operator import CloudSqlInstanceCreateOperator as CloudSqlInstanceCreateOperator, CloudSqlInstanceDatabaseCreateOperator as CloudSqlInstanceDatabaseCreateOperator, CloudSqlInstanceDatabaseDeleteOperator as CloudSqlInstanceDatabaseDeleteOperator, CloudSqlInstanceDatabasePatchOperator as CloudSqlInstanceDatabasePatchOperator, CloudSqlInstanceDeleteOperator as CloudSqlInstanceDeleteOperator, CloudSqlInstanceExportOperator as CloudSqlInstanceExportOperator, CloudSqlInstanceImportOperator as CloudSqlInstanceImportOperator, CloudSqlInstancePatchOperator as CloudSqlInstancePatchOperator
from airflow.contrib.operators.gcs_acl_operator import GoogleCloudStorageBucketCreateAclEntryOperator as GoogleCloudStorageBucketCreateAclEntryOperator, GoogleCloudStorageObjectCreateAclEntryOperator as GoogleCloudStorageObjectCreateAclEntryOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

GCP_PROJECT_ID: Any
INSTANCE_NAME: Any
INSTANCE_NAME2: Any
DB_NAME: Any
EXPORT_URI: Any
IMPORT_URI: Any
FAILOVER_REPLICA_NAME: Any
READ_REPLICA_NAME: Any
body: Any
body2: Any
read_replica_body: Any
patch_body: Any
export_body: Any
import_body: Any
db_create_body: Any
db_patch_body: Any
default_args: Any

def next_dep(task, prev): ...

sql_instance_create_task: Any
prev_task = sql_instance_create_task
sql_instance_create_2_task: Any
prev_task = sql_instance_create_task
sql_instance_read_replica_create: Any
sql_instance_patch_task: Any
sql_instance_patch_task2: Any
sql_db_create_task: Any
sql_db_create_task2: Any
sql_db_patch_task: Any
sql_db_patch_task2: Any
export_url_split: Any
sql_gcp_add_bucket_permission_task: Any
sql_export_task: Any
sql_export_task2: Any
import_url_split: Any
sql_gcp_add_object_permission_task: Any
sql_gcp_add_bucket_permission_2_task: Any
sql_import_task: Any
sql_import_task2: Any
sql_db_delete_task: Any
sql_db_delete_task2: Any
sql_instance_failover_replica_delete_task: Any
sql_instance_read_replica_delete_task: Any
sql_instance_delete_task: Any
sql_instance_delete_task2: Any
sql_instance_delete_2_task: Any
