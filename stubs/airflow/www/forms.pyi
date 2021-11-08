from airflow.utils import timezone as timezone
from flask_wtf import FlaskForm
from typing import Any

class DateTimeForm(FlaskForm):
    execution_date: Any

class DateTimeWithNumRunsForm(FlaskForm):
    base_date: Any
    num_runs: Any

class DateTimeWithNumRunsWithDagRunsForm(DateTimeWithNumRunsForm):
    execution_date: Any
