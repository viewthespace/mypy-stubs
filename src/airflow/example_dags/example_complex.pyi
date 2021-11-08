from airflow import models as models
from airflow.operators.bash_operator import BashOperator as BashOperator
from airflow.operators.python_operator import PythonOperator as PythonOperator
from airflow.utils.dates import days_ago as days_ago
from airflow.utils.helpers import chain as chain
from typing import Any

default_args: Any
create_entry_group: Any
create_entry_group_result: Any
create_entry_group_result2: Any
create_entry_gcs: Any
create_entry_gcs_result: Any
create_entry_gcs_result2: Any
create_tag: Any
create_tag_result: Any
create_tag_result2: Any
create_tag_template: Any
create_tag_template_result: Any
create_tag_template_result2: Any
create_tag_template_field: Any
create_tag_template_field_result: Any
create_tag_template_field_result2: Any
delete_entry: Any
delete_entry_group: Any
delete_tag: Any
delete_tag_template_field: Any
delete_tag_template: Any
get_entry_group: Any
get_entry_group_result: Any
get_entry: Any
get_entry_result: Any
get_tag_template: Any
get_tag_template_result: Any
list_tags: Any
list_tags_result: Any
lookup_entry: Any
lookup_entry_result: Any
rename_tag_template_field: Any
search_catalog: Any
search_catalog_result: Any
update_entry: Any
update_tag: Any
update_tag_template: Any
update_tag_template_field: Any
create_tasks: Any
delete_tasks: Any
