from airflow.contrib.hooks.imap_hook import ImapHook as ImapHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import apply_defaults as apply_defaults
from typing import Any

class ImapAttachmentSensor(BaseSensorOperator):
    template_fields: Any
    attachment_name: Any
    mail_folder: Any
    check_regex: Any
    conn_id: Any
    def __init__(self, attachment_name, mail_folder: str = ..., check_regex: bool = ..., conn_id: str = ..., *args, **kwargs) -> None: ...
    def poke(self, context): ...
