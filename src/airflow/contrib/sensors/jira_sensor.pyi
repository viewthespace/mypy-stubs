from airflow.contrib.operators.jira_operator import JIRAError as JIRAError, JiraOperator as JiraOperator
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class JiraSensor(BaseSensorOperator):
    jira_conn_id: Any
    result_processor: Any
    method_name: Any
    method_params: Any
    jira_operator: Any
    def __init__(self, jira_conn_id: str = ..., method_name: Any | None = ..., method_params: Any | None = ..., result_processor: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...

class JiraTicketSensor(JiraSensor):
    template_fields: Any
    jira_conn_id: Any
    ticket_id: Any
    field: Any
    expected_value: Any
    def __init__(self, jira_conn_id: str = ..., ticket_id: Any | None = ..., field: Any | None = ..., expected_value: Any | None = ..., field_checker_func: Any | None = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
    def issue_field_checker(self, context, issue): ...
