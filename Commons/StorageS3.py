import os
from typing import Any

import boto3
import botocore

from Settings import awsSettings


class StorageS3:
    def __init__(self, bucket_name='task-bucket-a') -> None:
        self.s3 = None
        self.bucket_name = bucket_name
        self.connect()

    def connect(self, access_key_id=awsSettings.access_key_id,
                secret_access_key=awsSettings.secret_access_key):

        self.s3 = boto3.resource('s3',
                                 aws_access_key_id=access_key_id,
                                 aws_secret_access_key=secret_access_key)

    def download_file(self, obj_name, file_name):
        try:
            self.s3.Bucket(self.bucket_name).download_file(obj_name, file_name)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

    def upload(self, file_name, directory: str) -> None:
        self.s3.meta.client.upload_file(file_name, self.bucket_name,
                                        '{directory}/{name}'.format(
                                            directory=directory,
                                            name=file_name)
                                        )
