from airflow.models import Log as Log
from airflow.utils import cli_action_loggers as cli_action_loggers
from airflow.utils.platform import is_terminal_support_colors as is_terminal_support_colors

def action_logging(f): ...

class ColorMode:
    ON: str
    OFF: str
    AUTO: str

def should_use_colors(args): ...
