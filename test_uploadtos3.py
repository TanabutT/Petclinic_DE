# from uploadfile_s3 import upload_file
import boto3


AWS_KEY_ID ="ASIAWFHJWX4C5UMGRA5Q"
AWS_SECRET = "iRjXkQUzA7dtLJPNE7w6pjRfxFT7GxIfy4G/p++u"

s3 = boto3.client('s3',
                    region_name='us-east-1',
                    aws_access_key_id=AWS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET)
response = s3.list_buckets()
print(response)

# pets_csv = "./P9-Pets.csv"
# upload_file(file_name=pets_csv, bucket)

