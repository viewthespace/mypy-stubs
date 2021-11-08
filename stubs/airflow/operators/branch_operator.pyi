from airflow.models import BaseOperator as BaseOperator, SkipMixin as SkipMixin
from typing import Dict, Iterable, Union

class BaseBranchOperator(BaseOperator, SkipMixin):
    def choose_branch(self, context: Dict) -> Union[str, Iterable[str]]: ...
    def execute(self, context) -> None: ...
