from airflow import DAG as DAG
from airflow.contrib.operators.dingding_operator import DingdingOperator as DingdingOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

args: Any

def failure_callback(context): ...

text_msg_remind_none: Any
text_msg_remind_specific: Any
text_msg_remind_include_invalid: Any
text_msg_remind_all: Any
link_msg: Any
markdown_msg: Any
single_action_card_msg: Any
multi_action_card_msg: Any
feed_card_msg: Any
msg_failure_callback: Any
