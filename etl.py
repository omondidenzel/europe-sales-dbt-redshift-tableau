import pandas as pd
from sqlalchemy import create_engine 
import boto3
import os
from botocore.exceptions import ClientError
import logging
from dotenv import load_dotenv


load_dotenv()

region_name = os.getenv('AWS_REGION_NAME')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')


def fileUpload(data):
    s3 = boto3.resource(
        service_name = 's3',
        region_name = region_name,
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key
    )

    # retrieve available bucket
    # for x in s3.buckets.all():
    #     print(x)

    # Upload file
    try:
        s3.Bucket('sales-bucket-denzel').upload_file(Filename=data,Key='europe-sales-data' )
        print('Europe sales uploaded')
     # To catch errors   
    except ClientError as e:
        print(e)
        return False

data = 'Europe Sales Records.csv'
fileUpload(data)