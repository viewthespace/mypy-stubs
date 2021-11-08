from airflow import models as models
from airflow.contrib.operators.gcp_function_operator import GcfFunctionDeleteOperator as GcfFunctionDeleteOperator, GcfFunctionDeployOperator as GcfFunctionDeployOperator
from airflow.utils import dates as dates
from typing import Any

GCP_PROJECT_ID: Any
GCP_LOCATION: Any
GCF_SHORT_FUNCTION_NAME: Any
FUNCTION_NAME: Any
GCF_SOURCE_ARCHIVE_URL: Any
GCF_SOURCE_UPLOAD_URL: Any
GCF_SOURCE_REPOSITORY: Any
GCF_ZIP_PATH: Any
GCF_ENTRYPOINT: Any
GCF_RUNTIME: str
GCP_VALIDATE_BODY: Any
body: Any
default_args: Any
deploy_task: Any
deploy2_task: Any
delete_task: Any
