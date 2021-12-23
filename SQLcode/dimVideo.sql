CREATE EXTERNAL TABLE IF NOT EXISTS `atestdb`.`dimVideo` (
 `channel_id` string,
 `channel_name` string,
 `title` string,
 `description` string,
 `category_id` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://task-bucket-a/Parquet/Video/dimVideo'
TBLPROPERTIES ('has_encrypted_data'='false')