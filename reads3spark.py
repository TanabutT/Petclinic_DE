from pyspark import SparkConf
from pyspark.sql import SparkSession

AWS_ACCESS_KEY_ID = "ASIAWFHJWX4CYHJBFV65"
AWS_SECRET_ACCESS_KEY = "kENd8eM8UTRTGML39PwYLrqWo/d/RUll9AIgCDBE"
AWS_SESSION_TOKEN = "FwoGZXIvYXdzEHAaDJqV/FpGSwhsqoZKoSLHAUoWbX1KrWnzSJkvrZ4nbi0+bpk4Nlk3FIaK8yC+jALna10Fwxp6qyd75fJk9J6EzsGNGfMVxeHTJrpz91sgUGXNSnEeI5SRUmMjiJ2ln9AjHhuq/TKIbv73eqjdXS9Mw81mQFZ6OVHBCBSnOlve3MLyZNG5Qb+BRZXkbq9qHxaP/1g2gvGqWnvCrhxZVo+vHmTuDA/YXWAYb+mAv2QSGZfWCFteNt6gukBTwxHvhqLgR7EIHsYDBILRWYPh+tuvhMj/94Igq+Qo1v3VnAYyLY0BwfqyngQPrQ44EvE0rFOw8D8EYctOFdsWLcTEq2L0UNDJJWa3V/hKglnG1w=="


conf = SparkConf()
conf.set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.2")
conf.set("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider")
conf.set("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY_ID)
conf.set("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_ACCESS_KEY)
conf.set("spark.hadoop.fs.s3a.session.token", AWS_SESSION_TOKEN)

spark = SparkSession.builder.config(conf=conf).getOrCreate()


df = spark.read.csv("s3://petclinic13/PetClinic_landing/P9-Pets.csv", header=True)

df.show()