from airflow import DAG as DAG
from airflow.contrib.operators.pubsub_operator import PubSubPublishOperator as PubSubPublishOperator, PubSubSubscriptionCreateOperator as PubSubSubscriptionCreateOperator, PubSubSubscriptionDeleteOperator as PubSubSubscriptionDeleteOperator, PubSubTopicCreateOperator as PubSubTopicCreateOperator, PubSubTopicDeleteOperator as PubSubTopicDeleteOperator
from airflow.contrib.sensors.pubsub_sensor import PubSubPullSensor as PubSubPullSensor
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.utils import dates as dates
from typing import Any

project: str
topic: str
subscription: str
messages: Any
default_args: Any
echo_template: str
t1: Any
t2: Any
t3: Any
t4: Any
t5: Any
t6: Any
t7: Any
