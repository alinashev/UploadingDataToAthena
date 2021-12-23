CREATE EXTERNAL TABLE IF NOT EXISTS `atestdb`.`factChannel` (
`channel_id` string,
 `date_id` string,
 `time_id` string,
 `view_count` bigint,
 `subscriber_count` bigint,
 `video_count` bigint
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://task-bucket-a/Parquet/Channel/factChannel'
TBLPROPERTIES ('has_encrypted_data'='false')