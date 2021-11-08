from airflow import models as models
from airflow.contrib.operators.gcs_acl_operator import GoogleCloudStorageBucketCreateAclEntryOperator as GoogleCloudStorageBucketCreateAclEntryOperator, GoogleCloudStorageObjectCreateAclEntryOperator as GoogleCloudStorageObjectCreateAclEntryOperator
from typing import Any

GCS_ACL_BUCKET: Any
GCS_ACL_OBJECT: Any
GCS_ACL_ENTITY: Any
GCS_ACL_BUCKET_ROLE: Any
GCS_ACL_OBJECT_ROLE: Any
default_args: Any
gcs_bucket_create_acl_entry_task: Any
gcs_object_create_acl_entry_task: Any
