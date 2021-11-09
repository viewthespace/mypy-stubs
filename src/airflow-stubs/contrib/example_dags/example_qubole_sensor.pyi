from airflow import DAG as DAG
from airflow.contrib.sensors.qubole_sensor import QuboleFileSensor as QuboleFileSensor, QubolePartitionSensor as QubolePartitionSensor
from airflow.utils import dates as dates
from typing import Any

default_args: Any
t1: Any
t2: Any
