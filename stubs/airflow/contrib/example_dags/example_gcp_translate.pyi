from airflow import models as models
from airflow.contrib.operators.gcp_translate_operator import CloudTranslateTextOperator as CloudTranslateTextOperator
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any
product_set_create: Any
translation_access: Any
