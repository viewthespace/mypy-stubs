from airflow.sensors.base_sensor_operator import BaseSensorOperator as BaseSensorOperatorImp
from airflow.sensors.external_task_sensor import ExternalTaskSensor as ExternalTaskSensorImp
from airflow.sensors.hdfs_sensor import HdfsSensor as HdfsSensorImp
from airflow.sensors.hive_partition_sensor import HivePartitionSensor as HivePartitionSensorImp
from airflow.sensors.http_sensor import HttpSensor as HttpSensorImp
from airflow.sensors.metastore_partition_sensor import MetastorePartitionSensor as MetastorePartitionSensorImp
from airflow.sensors.s3_key_sensor import S3KeySensor as S3KeySensorImp
from airflow.sensors.s3_prefix_sensor import S3PrefixSensor as S3PrefixSensorImp
from airflow.sensors.sql_sensor import SqlSensor as SqlSensorImp
from airflow.sensors.time_delta_sensor import TimeDeltaSensor as TimeDeltaSensorImp
from airflow.sensors.time_sensor import TimeSensor as TimeSensorImp
from airflow.sensors.web_hdfs_sensor import WebHdfsSensor as WebHdfsSensorImp

class BaseSensorOperator(BaseSensorOperatorImp): ...
class ExternalTaskSensor(ExternalTaskSensorImp): ...
class HdfsSensor(HdfsSensorImp): ...
class HttpSensor(HttpSensorImp): ...
class MetastorePartitionSensor(MetastorePartitionSensorImp): ...
class HivePartitionSensor(HivePartitionSensorImp): ...
class S3KeySensor(S3KeySensorImp): ...
class S3PrefixSensor(S3PrefixSensorImp): ...
class SqlSensor(SqlSensorImp): ...
class TimeDeltaSensor(TimeDeltaSensorImp): ...
class TimeSensor(TimeSensorImp): ...
class WebHdfsSensor(WebHdfsSensorImp): ...
