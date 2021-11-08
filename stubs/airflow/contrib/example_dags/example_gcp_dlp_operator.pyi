from airflow.contrib.operators.gcp_dlp_operator import CloudDLPCreateInspectTemplateOperator as CloudDLPCreateInspectTemplateOperator, CloudDLPDeleteInspectTemplateOperator as CloudDLPDeleteInspectTemplateOperator, CloudDLPInspectContentOperator as CloudDLPInspectContentOperator
from airflow.models import DAG as DAG
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any
GCP_PROJECT: Any
TEMPLATE_ID: str
ITEM: Any
INSPECT_CONFIG: Any
INSPECT_TEMPLATE: Any
create_template: Any
inspect_content: Any
delete_template: Any
