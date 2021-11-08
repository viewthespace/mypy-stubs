from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException, AirflowException as AirflowException
from typing import Any

log: Any
broker_url: Any
broker_transport_options: Any
DEFAULT_CELERY_CONFIG: Any
celery_ssl_active: bool
broker_use_ssl: Any
result_backend: Any
