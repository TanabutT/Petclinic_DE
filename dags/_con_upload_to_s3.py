import boto3


from airflow import DAG
from airflow.utils import timezone
from airflow.operators.python import PythonOperator
from settings_dags import aws_access_key_id , aws_secret_access_key , aws_session_token


def _con_upload_to_s3(**context):
    """ connect to s3 with boto3 and the get the filename list from ti-task instance send via xcom
    to get data whice require to transfer from local to s3 bucket
    """
    #connect s3 with python by boto3
    s3 = boto3.client('s3',
                    region_name='us-east-1',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token)

    ti = context["ti"]

    # get datetime
    curr_dt = context["ds"]

    # Get list of files from filepath
    all_files = ti.xcom_pull(task_ids="get_files", key="return_value")
    print("all_files : ", len(all_files))
    print("curr_dt : ", curr_dt)
    print("ti : ", ti)
    print(all_files)


    # create directory "PetClinic_landing" in bucket S3
    BUCKET_NAME = "petclinic13"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Body='',
        Key='PetClinic_landing/'
        )

    # upload filen to directory in bucket S3
    for filename in all_files:
        print("Putting %s" % filename)
        #check filename to keep in s3 after split()
        print("Putting %s" % filename.split("/")[-1])
        # s3.upload_file(filename, BUCKET_NAME, 'PetClinic_landing/' + filename.split("\\")[1]) # for os window
        s3.upload_file(filename, BUCKET_NAME, 'PetClinic_landing/' + filename.split("/")[-1]) # for os linux

    #list file in bucket after upload
    response = s3.list_objects(  Bucket='petclinic13',   
                            MaxKeys=4)  
                            # Prefix='P9')
    print(response)