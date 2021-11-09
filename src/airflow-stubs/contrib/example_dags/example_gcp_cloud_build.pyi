from airflow import models as models
from airflow.contrib.operators.gcp_cloud_build_operator import CloudBuildCreateBuildOperator as CloudBuildCreateBuildOperator
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.utils import dates as dates
from typing import Any

GCP_PROJECT_ID: Any
GCP_SOURCE_ARCHIVE_URL: Any
GCP_SOURCE_REPOSITORY_NAME: Any
GCP_SOURCE_ARCHIVE_URL_PARTS: Any
GCP_SOURCE_BUCKET_NAME: Any
create_build_from_storage_body: Any
create_build_from_repo_body: Any
create_build_from_storage: Any
create_build_from_storage_result: Any
create_build_from_repo: Any
create_build_from_repo_result: Any
