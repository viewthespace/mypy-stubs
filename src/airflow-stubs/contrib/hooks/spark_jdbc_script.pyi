def set_common_options(spark_source, url: str = ..., jdbc_table: str = ..., user: str = ..., password: str = ..., driver: str = ...): ...
def spark_write_to_jdbc(spark, url, user, password, metastore_table, jdbc_table, driver, truncate, save_mode, batch_size, num_partitions, create_table_column_types) -> None: ...
def spark_read_from_jdbc(spark, url, user, password, metastore_table, jdbc_table, driver, save_mode, save_format, fetch_size, num_partitions, partition_column, lower_bound, upper_bound) -> None: ...