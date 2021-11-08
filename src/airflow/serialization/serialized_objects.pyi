from airflow import AirflowException as AirflowException, DAG as DAG
from airflow.models.baseoperator import BaseOperator as BaseOperator, BaseOperatorLink as BaseOperatorLink
from airflow.models.connection import Connection as Connection
from airflow.serialization.enums import Encoding as Encoding
from airflow.serialization.helpers import serialize_template_field as serialize_template_field
from airflow.serialization.json_schema import Validator as Validator, load_dag_schema as load_dag_schema
from airflow.settings import json as json
from airflow.utils.module_loading import import_string as import_string
from airflow.www.utils import get_python_source as get_python_source
from typing import Any, List, Union

log: Any
BUILTIN_OPERATOR_EXTRA_LINKS: List[str]

class BaseSerialization:
    SERIALIZER_VERSION: int
    @classmethod
    def to_json(cls, var: Union[DAG, BaseOperator, dict, list, set, tuple]) -> str: ...
    @classmethod
    def to_dict(cls, var: Union[DAG, BaseOperator, dict, list, set, tuple]) -> dict: ...
    @classmethod
    def from_json(cls, serialized_obj: str) -> Union[BaseSerialization, dict, list, set, tuple]: ...
    @classmethod
    def from_dict(cls, serialized_obj: dict) -> Union[BaseSerialization, dict, list, set, tuple]: ...
    @classmethod
    def validate_schema(cls, serialized_obj: Union[str, dict]) -> None: ...
    @classmethod
    def serialize_to_json(cls, object_to_serialize, decorated_fields): ...

class SerializedBaseOperator(BaseOperator, BaseSerialization):
    ui_color: Any
    ui_fgcolor: Any
    template_fields: Any
    subdag: Any
    operator_extra_links: Any
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def task_type(self) -> str: ...
    @task_type.setter
    def task_type(self, task_type: str) -> None: ...
    @classmethod
    def serialize_operator(cls, op: BaseOperator) -> dict: ...
    @classmethod
    def deserialize_operator(cls, encoded_op: dict) -> BaseOperator: ...

class SerializedDAG(DAG, BaseSerialization):
    @classmethod
    def serialize_dag(cls, dag: DAG) -> dict: ...
    @classmethod
    def deserialize_dag(cls, encoded_dag: dict) -> SerializedDAG: ...
    @classmethod
    def to_dict(cls, var) -> dict: ...
    @classmethod
    def from_dict(cls, serialized_obj: dict) -> SerializedDAG: ...

FAILED: str
