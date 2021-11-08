from airflow.exceptions import AirflowSkipException as AirflowSkipException
from airflow.models import DAG as DAG
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

args: Any

class DummySkipOperator(DummyOperator):
    ui_color: str
    def execute(self, context) -> None: ...

def create_test_pipeline(suffix, trigger_rule, dag) -> None: ...

dag: Any
