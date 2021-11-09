from airflow import DAG as DAG
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.operators.hive_operator import HiveOperator as HiveOperator
from airflow.operators.python_operator import PythonOperator as PythonOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

def fetchtweets() -> None: ...
def cleantweets() -> None: ...
def analyzetweets() -> None: ...
def transfertodb() -> None: ...

default_args: Any
fetch_tweets: Any
clean_tweets: Any
analyze_tweets: Any
hive_to_mysql: Any
from_channels: Any
to_channels: Any
yesterday: Any
dt: Any
local_dir: str
hdfs_dir: str
file_name: Any
load_to_hdfs: Any
load_to_hive: Any
