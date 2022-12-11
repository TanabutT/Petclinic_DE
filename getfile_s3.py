import boto3
import glob
import pandas as pd
import pyarrow.parquet as pq
import s3fs
import pyspark 
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
from settings import aws_access_key_id , aws_secret_access_key , aws_session_token

s3filesystem = s3fs.S3FileSystem()


s3 = boto3.client('s3',
                    region_name='us-east-1',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token)

response = s3.get_object(Bucket="petclinic13", Key="cleaned_zone_parquet/owners.parquet")

status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
print(response.get("Body"))
if status == 200:
    print(f"Successful S3 get_object response. Status - {status}")
    # owners_df = pd.read_parquet(response.get("Body"), engine='pyarrow')
    owners_df = spark.read.parquet(response.get("Body"))
    # owners_df = pq.ParquetDataset('s3://petclinic13/cleaned_zone_parquet/owners.parquet/part-00000-c77ed904-45d9-4dc7-b9b5-89c7d676e8e0-c000.snappy.parquet', 
    #                                 filesystem=s3filesystem).read_pandas().to_pandas()
    print(owners_df)
else:
    print(f"Unsuccessful S3 get_object response. Status - {status}")