import boto3
import pickle
from datetime import datetime
from settings import * 

client = boto3.client('redshift',

                        region_name='us-east-1',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token)

response = client.delete_cluster(
    ClusterIdentifier='redshift-cluster-petclinic'
    ,SkipFinalClusterSnapshot=True
    #,FinalClusterSnapshotIdentifier='string'
)
