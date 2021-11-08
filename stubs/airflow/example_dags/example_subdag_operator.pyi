from airflow.example_dags.subdags.subdag import subdag as subdag
from airflow.models import DAG as DAG
from airflow.operators.dummy_operator import DummyOperator as DummyOperator
from airflow.operators.subdag_operator import SubDagOperator as SubDagOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

DAG_NAME: str
args: Any
dag: Any
start: Any
section_1: Any
some_other_task: Any
section_2: Any
end: Any
