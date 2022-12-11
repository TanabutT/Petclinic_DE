import boto3
import glob

AWS_ACCESS_KEY_ID = "ASIAWFHJWX4C5UMGRA5Q"
AWS_SECRET_ACCESS_KEY = "iRjXkQUzA7dtLJPNE7w6pjRfxFT7GxIfy4G/p++u"
AWS_SESSION_TOKEN = "FwoGZXIvYXdzEGAaDOCn4A3NrFWrlc+FxiLHAUni2WVfPzcdHXDl3nDao3w670Dy72mFaoogYYN/BcbCJ+vGUmfluFD61BkL9e6fYKGljqo32I6uhBHOHGabXUKaXvXkX/AcEcnO+bTXEirQwVeyiOm82LyeFYTeuXJ9wtyMyWNLNtCQTwHJAzlZW6q6Hg61/3huJOfYzZ2zbX24lCVzP65zF03Uk4rDGbowG+Ai7OtgVmE4thpuNiZr+Na1ElfyXnKIyBNojmCAZMTSCURl4lsLA1sfoE/lxQB5+OQ+3AwlmzQowbDSnAYyLb1dR1SD7N1NuAce/+thKd6og+lJx70fsLlu1hgYwnQw/1gxGW4u4XM5YBU6zQ=="
BUCKET_NAME='petclinic13'


s3 = boto3.client('s3',
                    region_name='us-east-1',
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    aws_session_token=AWS_SESSION_TOKEN)

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
    s3.upload_file(filename, BUCKET_NAME, 'PetClinic_landing/' + filename.split("\\")[1])

# s3.upload_file(  Filename='PetClinicdata\P9-ProceduresDetails.csv',
#                     Bucket='petclinic13',   
#                     Key='Pets/P9-ProceduresDetails.csv')

response = s3.list_objects(  Bucket='petclinic13',   
                            MaxKeys=4)  
                            # Prefix='P9')
print(response)

