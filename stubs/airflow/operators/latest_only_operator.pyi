from airflow.models import BaseOperator as BaseOperator, SkipMixin as SkipMixin

class LatestOnlyOperator(BaseOperator, SkipMixin):
    ui_color: str
    def execute(self, context) -> None: ...
