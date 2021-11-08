from airflow.contrib.hooks.winrm_hook import WinRMHook as WinRMHook
from airflow.contrib.operators.winrm_operator import WinRMOperator as WinRMOperator
from airflow.models import DAG as DAG
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any
cmd: str
run_this_last: Any
winRMHook: Any
t1: Any
t2: Any
t3: Any
