from airflow.models import DAG as DAG
from airflow.operators.dummy_operator import DummyOperator as DummyOperator

def subdag(parent_dag_name, child_dag_name, args): ...
