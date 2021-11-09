from airflow import AirflowException as AirflowException, LoggingMixin as LoggingMixin
from typing import Any, Dict, Sequence

COMPOSITE_FIELD_TYPES: Any

class GcpFieldValidationException(AirflowException):
    def __init__(self, message) -> None: ...

class GcpValidationSpecificationException(AirflowException):
    def __init__(self, message) -> None: ...

EXAMPLE_VALIDATION_SPECIFICATION: Any

class GcpBodyFieldValidator(LoggingMixin):
    def __init__(self, validation_specs: Sequence[Dict], api_version: str) -> None: ...
    def validate(self, body_to_validate) -> None: ...
