from airflow import DAG as DAG
from airflow.contrib.operators.azure_cosmos_operator import AzureCosmosInsertDocumentOperator as AzureCosmosInsertDocumentOperator
from airflow.contrib.sensors.azure_cosmos_sensor import AzureCosmosDocumentSensor as AzureCosmosDocumentSensor
from airflow.utils import dates as dates
from typing import Any

default_args: Any
t1: Any
t2: Any
