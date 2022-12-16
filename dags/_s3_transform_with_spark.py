from pyspark import SparkConf
from pyspark.sql import SparkSession
from settings import aws_access_key_id , aws_secret_access_key , aws_session_token

def _s3_transform_with_spark():
    """
    This function Use pyspark to read csv file in s3 landing zone then clean and transform 
    to .parquet file and keep it in folder cleaned_zone_parquet prepare for redshift cluster get data 
    """

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

    pets_table.write.mode("overwrite").parquet("s3a://petclinic13/cleaned_zone_parquet/pets.parquet")
    owners_table.write.mode("overwrite").parquet("s3a://petclinic13/cleaned_zone_parquet/owners.parquet")
    pdetail_table.write.mode("overwrite").parquet("s3a://petclinic13/cleaned_zone_parquet/pdetail.parquet")
    phistory_table.write.mode("overwrite").parquet("s3a://petclinic13/cleaned_zone_parquet/phistory.parquet")
    print("#### write parquet file to cleaned_zone_parquet directory completed #####")