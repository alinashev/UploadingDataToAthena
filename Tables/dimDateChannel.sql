CREATE EXTERNAL TABLE IF NOT EXISTS `atestdb`.`dimDateChanne` (
 `date_id` string,
 `year` int,
 `month` int,
 `day` int,
 `week` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://task-bucket-a/Parquet/{dir}/Channel/dimDateChannel'
TBLPROPERTIES ('has_encrypted_data'='false')