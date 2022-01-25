CREATE EXTERNAL TABLE IF NOT EXISTS `a-test-db-01`.`dimChannel` (
`channel_id` string,
 `channel_name` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://{bucket}/Data/Channel/DimChannel'
TBLPROPERTIES ('has_encrypted_data'='false')