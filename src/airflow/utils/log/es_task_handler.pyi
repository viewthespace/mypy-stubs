from airflow.configuration import conf as conf
from airflow.utils import timezone as timezone
from airflow.utils.helpers import parse_template_string as parse_template_string
from airflow.utils.log.file_task_handler import FileTaskHandler as FileTaskHandler
from airflow.utils.log.json_formatter import JSONFormatter as JSONFormatter
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

class ElasticsearchTaskHandler(FileTaskHandler, LoggingMixin):
    PAGE: int
    MAX_LINE_PER_PAGE: int
    closed: bool
    client: Any
    mark_end_on_close: bool
    end_of_log_mark: Any
    write_stdout: Any
    json_format: Any
    json_fields: Any
    handler: Any
    context_set: bool
    def __init__(self, base_log_folder, filename_template, log_id_template, end_of_log_mark, write_stdout, json_format, json_fields, host: str = ..., es_kwargs=...) -> None: ...
    def es_read(self, log_id, offset, metadata): ...
    formatter: Any
    def set_context(self, ti) -> None: ...
    def close(self) -> None: ...
