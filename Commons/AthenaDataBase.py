from typing import Any
from pyathena import connect

from Settings import awsSettings


class AthenaDataBase:
    def __init__(self):
        self.connection = None

    def connect(self,
                aws_access_key_id=awsSettings.access_key_id,
                aws_secret_access_key=awsSettings.secret_access_key,
                s3_staging_dir='s3://task-bucket-a/athena-result/',
                region_name='us-east-2') -> Any:
        try:
            self.connection = connect(aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                      s3_staging_dir=s3_staging_dir,
                                      region_name=region_name)
        except Exception as error:
            print(error)
        return self.connection
