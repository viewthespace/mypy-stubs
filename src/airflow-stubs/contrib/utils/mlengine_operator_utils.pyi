from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook as GoogleCloudStorageHook
from airflow.contrib.operators.dataflow_operator import DataFlowPythonOperator as DataFlowPythonOperator
from airflow.contrib.operators.mlengine_operator import MLEngineBatchPredictionOperator as MLEngineBatchPredictionOperator
from airflow.exceptions import AirflowException as AirflowException
from airflow.operators.python_operator import PythonOperator as PythonOperator
from typing import Any

def create_evaluate_ops(task_prefix, data_format, input_paths, prediction_path, metric_fn_and_keys, validate_fn, batch_prediction_job_id: Any | None = ..., project_id: Any | None = ..., region: Any | None = ..., dataflow_options: Any | None = ..., model_uri: Any | None = ..., model_name: Any | None = ..., version_name: Any | None = ..., dag: Any | None = ...): ...
