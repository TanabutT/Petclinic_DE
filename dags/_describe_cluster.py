import boto3
import pickle
from datetime import datetime
from settings_dags import * 

def _describe_cluster(**context):
        client = boto3.client('redshift',

                                region_name='us-east-1',
                                aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key,
                                aws_session_token=aws_session_token)

        ti = context["ti"]
        # Get list of files from filepath
        ClusterIdentifier = ti.xcom_pull(task_ids="create_Redshift", key="return_value")
        # print("ClusterIdentifier to  fill in response: ", ClusterIdentifier)
        """ClusterIdentifier will return "redshift-cluster-petclinic" that we name when create cluster"""

        response = client.describe_clusters(ClusterIdentifier=ClusterIdentifier, MaxRecords=100,)
        ClusterEndpoint = response['Clusters'][0]['Endpoint']['Address']
        print("ClusterIdentifier :" ,
                response['Clusters'][0]['ClusterIdentifier']
                )
        print("ClusterEndpoint : ", ClusterEndpoint)
        # print("ClusterEndpoint : ",
        #         response['Clusters'][0]['Endpoint']['Address']
        #         )
        return ClusterEndpoint