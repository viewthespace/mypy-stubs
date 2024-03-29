from airflow import models as models
from airflow.contrib.operators.gcp_video_intelligence_operator import CloudVideoIntelligenceDetectVideoExplicitContentOperator as CloudVideoIntelligenceDetectVideoExplicitContentOperator, CloudVideoIntelligenceDetectVideoLabelsOperator as CloudVideoIntelligenceDetectVideoLabelsOperator, CloudVideoIntelligenceDetectVideoShotsOperator as CloudVideoIntelligenceDetectVideoShotsOperator
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.utils.dates import days_ago as days_ago
from typing import Any

default_args: Any
GCP_BUCKET_NAME: Any
INPUT_URI: Any
detect_video_label: Any
detect_video_label_result: Any
detect_video_explicit_content: Any
detect_video_explicit_content_result: Any
detect_video_shots: Any
detect_video_shots_result: Any
