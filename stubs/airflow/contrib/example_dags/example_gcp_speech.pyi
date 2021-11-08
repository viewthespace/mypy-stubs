from airflow import models as models
from airflow.contrib.operators.gcp_speech_to_text_operator import GcpSpeechToTextRecognizeSpeechOperator as GcpSpeechToTextRecognizeSpeechOperator
from airflow.contrib.operators.gcp_text_to_speech_operator import GcpTextToSpeechSynthesizeOperator as GcpTextToSpeechSynthesizeOperator
from airflow.contrib.operators.gcp_translate_speech_operator import GcpTranslateSpeechOperator as GcpTranslateSpeechOperator
from airflow.utils import dates as dates
from typing import Any

GCP_PROJECT_ID: Any
BUCKET_NAME: Any
FILENAME: str
INPUT: Any
VOICE: Any
AUDIO_CONFIG: Any
CONFIG: Any
AUDIO: Any
TARGET_LANGUAGE: str
FORMAT: str
MODEL: str
SOURCE_LANGUAGE: Any
default_args: Any
text_to_speech_synthesize_task: Any
speech_to_text_recognize_task: Any
translate_speech_task: Any
