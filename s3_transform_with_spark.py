from pyspark import SparkConf
from pyspark.sql import SparkSession
from settings import aws_access_key_id , aws_secret_access_key , aws_session_token


conf = SparkConf()
conf.set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.2")
conf.set("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider")
conf.set("spark.hadoop.fs.s3a.access.key", aws_access_key_id)
conf.set("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key)
conf.set("spark.hadoop.fs.s3a.session.token", aws_session_token)

spark = SparkSession.builder.config(conf=conf).getOrCreate()

pets_df = spark.read.csv("s3a://petclinic13/PetClinic_landing/P9-Pets.csv", header=True)
owners_df = spark.read.csv("s3a://petclinic13/PetClinic_landing/P9-Owners.csv", header=True)
pdetail_df = spark.read.csv("s3a://petclinic13/PetClinic_landing/P9-ProceduresDetails.csv", header=True)
phistory_df = spark.read.csv("s3a://petclinic13/PetClinic_landing/P9-ProceduresHistory1.csv", header=True)


pets_df.createOrReplaceTempView("pets")
owners_df.createOrReplaceTempView("owners")
pdetail_df.createOrReplaceTempView("pdetail")
phistory_df.createOrReplaceTempView("phistory")

pets_table = spark.sql("""
    select
        PetID
        , Kind
        , Gender
        , Age
        , OwnerID
        
    from
        pets
""")



owners_table = spark.sql("""
    select
        *
                
    from
        owners
""")


pdetail_table = spark.sql("""
    select
        *
                
    from
        pdetail
""")

phistory_table = spark.sql("""
    select
        *
                
    from
        phistory
""")

pets_table.write.mode("overwrite").csv("s3a://petclinic13/pets.parquet")
owners_table.write.mode("overwrite").csv("s3a://petclinic13/owners.parquet")
pdetail_table.write.mode("overwrite").csv("s3a://petclinic13/pdetail.parquet")
phistory_table.write.mode("overwrite").csv("s3a://petclinic13/phistory.parquet")