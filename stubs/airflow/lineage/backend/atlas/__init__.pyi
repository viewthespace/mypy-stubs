from airflow.configuration import conf as conf
from airflow.lineage import datasets as datasets
from airflow.lineage.backend import LineageBackend as LineageBackend
from airflow.lineage.backend.atlas.typedefs import operator_typedef as operator_typedef
from airflow.utils.timezone import convert_to_utc as convert_to_utc

SERIALIZED_DATE_FORMAT_STR: str

class AtlasBackend(LineageBackend):
    @staticmethod
    def send_lineage(operator, inlets, outlets, context) -> None: ...
