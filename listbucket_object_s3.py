# from uploadfile_s3 import upload_file
import boto3
from settings import aws_access_key_id , aws_secret_access_key , aws_session_token

s3 = boto3.client('s3',
                    region_name='us-east-1',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token)
                    
response = s3.list_buckets()

print(response['Buckets'])

response1 = s3.list_objects(Bucket=response['Buckets'][0]['Name'])

# print(*[obj['Key'] for obj in response1['Contents']])

for obj in response1['Contents']:
    print(obj['Key'])

# print(response1['Contents'][0])

# pets_csv = "./P9-Pets.csv"
# upload_file(file_name=pets_csv, bucket)

