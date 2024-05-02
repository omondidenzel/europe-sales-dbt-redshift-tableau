import pandas as pd
from sqlalchemy import create_engine 
import boto3
import os
from botocore.exceptions import ClientError
import logging
from dotenv import load_dotenv


load_dotenv()

db_password = os.getenv('DB_PASSWORD')
region_name = os.getenv('AWS_REGION_NAME')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

print(aws_secret_access_key)

# # create connection engine
# username = 'admin'
# password = 'R1m7Xs6#O1bnyhoP'
# port = 5439
# db = 'sales'

# endpoint = 'postgresql://{}:{}@default-workgroup.276527400122.us-east-1.redshift-serverless.amazonaws.com:{}/{}'.format(username,password,port,db)
# # print(endpoint)
# conn = create_engine(endpoint)

# # Read data set 
# def read_dataset(data):
#     df = pd.read_csv(data)
#     print(conn)
#     # push data to database
#     df.to_sql('europe', conn, if_exists='replace', index=False)
    
# data = 'Europe Sales Records.csv'
# read_dataset(data)

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