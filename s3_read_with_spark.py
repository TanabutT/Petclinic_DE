from pyspark import SparkConf
from pyspark.sql import SparkSession

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_SESSION_TOKEN = ""

conf = SparkConf()
conf.set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.2")
conf.set("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider")
conf.set("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY_ID)
conf.set("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_ACCESS_KEY)
conf.set("spark.hadoop.fs.s3a.session.token", AWS_SESSION_TOKEN)

spark = SparkSession.builder.config(conf=conf).getOrCreate()


df = spark.read.csv("s3a://petclinic13/PetClinic_landing/P9-Pets.csv", header=True)

df.show()