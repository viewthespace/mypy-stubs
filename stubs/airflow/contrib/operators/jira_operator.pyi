from airflow.contrib.hooks.jira_hook import JIRAError as JIRAError, JiraHook as JiraHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class JiraOperator(BaseOperator):
    template_fields: Any
    jira_conn_id: Any
    method_name: Any
    jira_method_args: Any
    result_processor: Any
    get_jira_resource_method: Any
    def __init__(self, jira_conn_id: str = ..., jira_method: Any | None = ..., jira_method_args: Any | None = ..., result_processor: Any | None = ..., get_jira_resource_method: Any | None = ..., *args, **kwargs) -> None: ...
    def execute(self, context): ...
