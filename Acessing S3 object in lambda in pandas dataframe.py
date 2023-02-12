import boto3
import pandas as pd
from io import BytesIO
s3=boto3.resource('s3')

def lambda_handler(event,context):
  print(event)
  try:
    s3_bucket_name=event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name=event["Records"][0]["s3"]["object"]["key"]
    
    resp=s3.client.get_object(bucket= s3_bucket_name, Key= s3_file_name)
    print(resp["Body"])
    
    df_s3_data= p.read_csv(resp["Body"], sep=',')
    print(df_s3_data.head())
   except Exception as err:
    print(err)
