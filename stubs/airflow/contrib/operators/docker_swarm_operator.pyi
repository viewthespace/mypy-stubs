from airflow.exceptions import AirflowException as AirflowException
from airflow.operators.docker_operator import DockerOperator as DockerOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.strings import get_random_string as get_random_string
from typing import Any

class DockerSwarmOperator(DockerOperator):
    service: Any
    def __init__(self, image, *args, **kwargs) -> None: ...
    def on_kill(self) -> None: ...
