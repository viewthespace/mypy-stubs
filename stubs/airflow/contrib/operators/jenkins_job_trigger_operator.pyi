from airflow.contrib.hooks.jenkins_hook import JenkinsHook as JenkinsHook
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

def jenkins_request_with_headers(jenkins_server, req): ...

class JenkinsJobTriggerOperator(BaseOperator):
    template_fields: Any
    template_ext: Any
    ui_color: str
    job_name: Any
    parameters: Any
    sleep_time: Any
    jenkins_connection_id: Any
    max_try_before_job_appears: Any
    def __init__(self, jenkins_connection_id, job_name, parameters: str = ..., sleep_time: int = ..., max_try_before_job_appears: int = ..., *args, **kwargs) -> None: ...
    def build_job(self, jenkins_server): ...
    def poll_job_in_queue(self, location, jenkins_server): ...
    def get_hook(self): ...
    def execute(self, context): ...
