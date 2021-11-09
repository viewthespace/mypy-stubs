from airflow.configuration import conf as conf
from flask_appbuilder.security.manager import AUTH_DB
from typing import Any

basedir: Any
SQLALCHEMY_DATABASE_URI: Any
WTF_CSRF_ENABLED: bool
AUTH_TYPE = AUTH_DB
