CREATE EXTERNAL TABLE IF NOT EXISTS `a-test-db-01`.`dimTimeChannel` (
 `time_id` string,
 `hour` int,
 `minute` int,
 `second` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://task-bucket-a/Parquet/{dir}/Channel/dimTimeChannel'
TBLPROPERTIES ('has_encrypted_data'='false')