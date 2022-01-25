CREATE EXTERNAL TABLE IF NOT EXISTS `a-test-db-01`.`test` (
`col1` int, `col2` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' WITH SERDEPROPERTIES ( 'serialization.format' = '1'
) LOCATION 's3://task-bucket-a/Parquet/{dir}'
TBLPROPERTIES ('has_encrypted_data'='false')