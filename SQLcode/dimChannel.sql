CREATE EXTERNAL TABLE IF NOT EXISTS `atestdb`.`dimChannel` (
`channel_id` string,
 `channel_name` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://task-bucket-a/Parquet/Channel/dimChannel'
TBLPROPERTIES ('has_encrypted_data'='false')