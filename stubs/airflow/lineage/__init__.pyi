from airflow.configuration import conf as conf
from airflow.lineage.datasets import DataSet as DataSet
from airflow.utils.module_loading import import_string as import_string
from typing import Any

PIPELINE_OUTLETS: str
PIPELINE_INLETS: str
log: Any

def apply_lineage(func): ...
def prepare_lineage(func): ...
