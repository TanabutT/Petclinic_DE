import boto3
import glob
from settings import aws_access_key_id , aws_secret_access_key , aws_session_token

s3 = boto3.client('s3',
                    region_name='us-east-1',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token)

csv_files = glob.glob("PetClinicdata/*.csv")

# create directory "PetClinic_landing" in bucket S3
s3.put_object(
        Bucket=BUCKET_NAME,
        Body='',
        Key='PetClinic_landing/'
        )
        
# upload filen to directory in bucket S3
for filename in csv_files:
    print("Putting %s" % filename)
    # s3.upload_file(filename, BUCKET_NAME, 'PetClinic_landing/' + filename.split("\\")[1]) # for os window
    s3.upload_file(filename, BUCKET_NAME, 'PetClinic_landing/' + filename.split("/")[1]) # for os linux

# s3.upload_file(  Filename='PetClinicdata\P9-ProceduresDetails.csv',
#                     Bucket='petclinic13',   
#                     Key='Pets/P9-ProceduresDetails.csv')

response = s3.list_objects(  Bucket='petclinic13',   
                            MaxKeys=4)  
                            # Prefix='P9')
print(response)

