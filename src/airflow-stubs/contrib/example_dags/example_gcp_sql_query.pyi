from airflow import models as models
from airflow.contrib.operators.gcp_sql_operator import CloudSqlQueryOperator as CloudSqlQueryOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

GCP_PROJECT_ID: Any
GCP_REGION: Any
GCSQL_POSTGRES_INSTANCE_NAME_QUERY: Any
GCSQL_POSTGRES_DATABASE_NAME: Any
GCSQL_POSTGRES_USER: Any
GCSQL_POSTGRES_PASSWORD: Any
GCSQL_POSTGRES_PUBLIC_IP: Any
GCSQL_POSTGRES_PUBLIC_PORT: Any
GCSQL_POSTGRES_CLIENT_CERT_FILE: Any
GCSQL_POSTGRES_CLIENT_KEY_FILE: Any
GCSQL_POSTGRES_SERVER_CA_FILE: Any
GCSQL_MYSQL_INSTANCE_NAME_QUERY: Any
GCSQL_MYSQL_DATABASE_NAME: Any
GCSQL_MYSQL_USER: Any
GCSQL_MYSQL_PASSWORD: Any
GCSQL_MYSQL_PUBLIC_IP: Any
GCSQL_MYSQL_PUBLIC_PORT: Any
GCSQL_MYSQL_CLIENT_CERT_FILE: Any
GCSQL_MYSQL_CLIENT_KEY_FILE: Any
GCSQL_MYSQL_SERVER_CA_FILE: Any
SQL: Any
default_args: Any
HOME_DIR: Any

def get_absolute_path(path): ...

postgres_kwargs: Any
mysql_kwargs: Any
sql_proxy_binary_path: Any
connection_names: Any
tasks: Any
prev_task: Any
task: Any
prev_task = task
