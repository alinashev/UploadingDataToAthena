CREATE EXTERNAL TABLE IF NOT EXISTS `a-test-db-01`.`dimVideo` (
 `channel_id` string,
 `channel_name` string,
 `video_id` string,
 `title` string,
 `description` string,
 `category_id` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ('serialization.format' = '1'
) LOCATION 's3://{bucket}/Data/Video/DimVideo'
TBLPROPERTIES ('has_encrypted_data'='false')