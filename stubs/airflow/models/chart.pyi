from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.models.user import User as User
from airflow.utils import timezone as timezone
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import Any

class Chart(Base):
    __tablename__: str
    id: Any
    label: Any
    conn_id: Any
    user_id: Any
    chart_type: Any
    sql_layout: Any
    sql: Any
    y_log_scale: Any
    show_datatable: Any
    show_sql: Any
    height: Any
    default_params: Any
    owner: Any
    x_is_date: Any
    iteration_no: Any
    last_modified: Any
