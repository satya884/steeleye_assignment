# -*- coding: utf-8 -*-
from io import StringIO
import time
import pandas as pd
import os
import boto3

bucket = 's3-bucket-test-data'
key = 'csv-file/testfile.csv'

s3 = boto3.client('s3', aws_access_key_id='AKIAQGSTRFANJUYYQRB5', aws_secret_access_key='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')

print("create s3 client")
s3_resource = boto3.resource('s3')
s3_object = s3_resource.Object(bucket, key)

#fileKey = 'C:\py_code\xmlfile\testfile.csv'
df = pd.read_csv(r"E:\all files_satya\6th_sem\int233\data_gov.csv")
#print(df.to_string())

csv_buf = StringIO()
df.to_csv(csv_buf, header=True, index=False)
csv_buf.seek(0)
s3.put_object(Bucket=bucket, Body=csv_buf.getvalue(), Key=key)
print('S3: file is uploaded.')