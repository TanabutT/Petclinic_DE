import boto3
import glob
import pandas as pd
from settings import aws_access_key_id , aws_secret_access_key , aws_session_token

s3 = boto3.client('s3',
                    region_name='us-east-1',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token)

