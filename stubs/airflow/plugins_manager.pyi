from airflow import settings as settings
from airflow.models.baseoperator import BaseOperatorLink as BaseOperatorLink
from typing import Any, Dict, List, Type

log: Any
import_errors: Any

class AirflowPluginException(Exception): ...

class AirflowPlugin:
    name: str
    operators: List[Any]
    sensors: List[Any]
    hooks: List[Any]
    executors: List[Any]
    macros: List[Any]
    admin_views: List[Any]
    flask_blueprints: List[Any]
    menu_links: List[Any]
    appbuilder_views: List[Any]
    appbuilder_menu_items: List[Any]
    global_operator_extra_links: List[BaseOperatorLink]
    operator_extra_links: List[BaseOperatorLink]
    @classmethod
    def validate(cls) -> None: ...
    @classmethod
    def on_load(cls, *args, **kwargs) -> None: ...

def load_entrypoint_plugins(entry_points, airflow_plugins): ...
def is_valid_plugin(plugin_obj, existing_plugins): ...

plugins: List[AirflowPlugin]
norm_pattern: Any
filepath: Any
mod_name: Any
file_ext: Any
namespace: Any
m: Any

def make_module(name, objects): ...

operators_modules: Any
sensors_modules: Any
hooks_modules: Any
executors_modules: Any
macros_modules: Any
admin_views: List[Any]
flask_blueprints: List[Any]
menu_links: List[Any]
flask_appbuilder_views: List[Any]
flask_appbuilder_menu_links: List[Any]
global_operator_extra_links: List[BaseOperatorLink]
operator_extra_links: List[BaseOperatorLink]
registered_operator_link_classes: Dict[str, Type]
