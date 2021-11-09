from airflow.configuration import conf as conf
from sqlalchemy.types import TypeDecorator
from typing import Any

log: Any
utc: Any
using_mysql: Any

def setup_event_handlers(engine) -> None: ...

class UtcDateTime(TypeDecorator):
    impl: Any
    def process_bind_param(self, value, dialect): ...
    def process_result_value(self, value, dialect): ...

class Interval(TypeDecorator):
    impl: Any
    attr_keys: Any
    def process_bind_param(self, value, dialect): ...
    def process_result_value(self, value, dialect): ...
