from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults

class DummyOperator(BaseOperator):
    ui_color: str
    def __init__(self, *args, **kwargs) -> None: ...
    def execute(self, context) -> None: ...
