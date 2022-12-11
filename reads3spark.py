from pyspark import SparkConf
from pyspark.sql import SparkSession

AWS_ACCESS_KEY_ID = "ASIAWFHJWX4C5UMGRA5Q"
AWS_SECRET_ACCESS_KEY = "iRjXkQUzA7dtLJPNE7w6pjRfxFT7GxIfy4G/p++u"
AWS_SESSION_TOKEN = "FwoGZXIvYXdzEGAaDOCn4A3NrFWrlc+FxiLHAUni2WVfPzcdHXDl3nDao3w670Dy72mFaoogYYN/BcbCJ+vGUmfluFD61BkL9e6fYKGljqo32I6uhBHOHGabXUKaXvXkX/AcEcnO+bTXEirQwVeyiOm82LyeFYTeuXJ9wtyMyWNLNtCQTwHJAzlZW6q6Hg61/3huJOfYzZ2zbX24lCVzP65zF03Uk4rDGbowG+Ai7OtgVmE4thpuNiZr+Na1ElfyXnKIyBNojmCAZMTSCURl4lsLA1sfoE/lxQB5+OQ+3AwlmzQowbDSnAYyLb1dR1SD7N1NuAce/+thKd6og+lJx70fsLlu1hgYwnQw/1gxGW4u4XM5YBU6zQ=="


conf = SparkConf()
conf.set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.2")
conf.set("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider")
conf.set("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY_ID)
conf.set("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_ACCESS_KEY)
conf.set("spark.hadoop.fs.s3a.session.token", AWS_SESSION_TOKEN)

spark = SparkSession.builder.config(conf=conf).getOrCreate()


df = spark.read.csv("s3://petclinic13/PetClinic_landing/P9-Pets.csv", header=True)

df.show()