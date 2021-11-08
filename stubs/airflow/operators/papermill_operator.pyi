from airflow.lineage.datasets import DataSet as DataSet
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class NoteBook(DataSet):
    type_name: str
    attributes: Any

class PapermillOperator(BaseOperator):
    def __init__(self, input_nb, output_nb, parameters, *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
