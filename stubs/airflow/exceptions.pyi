from airflow.utils.code_utils import prepare_code_snippet as prepare_code_snippet
from airflow.utils.platform import is_tty as is_tty
from typing import Any, NamedTuple

class AirflowException(Exception):
    status_code: int

class AirflowBadRequest(AirflowException):
    status_code: int

class AirflowNotFoundException(AirflowException):
    status_code: int

class AirflowConfigException(AirflowException): ...
class AirflowSensorTimeout(AirflowException): ...

class AirflowRescheduleException(AirflowException):
    reschedule_date: Any
    def __init__(self, reschedule_date) -> None: ...

class AirflowTaskTimeout(AirflowException): ...
class AirflowWebServerTimeout(AirflowException): ...
class AirflowSkipException(AirflowException): ...
class AirflowFailException(AirflowException): ...
class AirflowDagCycleException(AirflowException): ...
class AirflowClusterPolicyViolation(AirflowException): ...
class DagNotFound(AirflowNotFoundException): ...
class DagCodeNotFound(AirflowNotFoundException): ...
class DagRunNotFound(AirflowNotFoundException): ...
class DagRunAlreadyExists(AirflowBadRequest): ...
class DagFileExists(AirflowBadRequest): ...
class TaskNotFound(AirflowNotFoundException): ...
class TaskInstanceNotFound(AirflowNotFoundException): ...
class PoolNotFound(AirflowNotFoundException): ...
class NoAvailablePoolSlot(AirflowException): ...
class DagConcurrencyLimitReached(AirflowException): ...
class TaskConcurrencyLimitReached(AirflowException): ...

class file_syntax_error(NamedTuple):
    line_no: Any
    message: Any

class AirflowFileParseException(AirflowException):
    msg: Any
    file_path: Any
    parse_errors: Any
    def __init__(self, msg, file_path, parse_errors) -> None: ...
