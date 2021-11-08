from airflow import models as models
from airflow.contrib.operators.gcs_to_gdrive_operator import GcsToGDriveOperator as GcsToGDriveOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

GCS_TO_GDRIVE_BUCKET: Any
default_args: Any
copy_single_file: Any
copy_files: Any
move_files: Any
