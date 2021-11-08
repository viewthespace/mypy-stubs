from airflow import DAG as DAG
from airflow.operators.http_operator import SimpleHttpOperator as SimpleHttpOperator
from airflow.sensors.http_sensor import HttpSensor as HttpSensor
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any
dag: Any
t1: Any
t5: Any
t2: Any
t3: Any
t4: Any
sensor: Any
