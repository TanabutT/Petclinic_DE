import boto3
import pickle
from datetime import datetime
from settings_dags import * 

def _create_Redshift():  
    redshift = boto3.client('redshift',

                        region_name='us-east-1',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token)

    ClusterIdentifier = "redshift-cluster-petclinic"
    response = redshift.create_cluster(
        DBName='petclinic',
        ClusterIdentifier=ClusterIdentifier,
        ClusterType='single-node',
        NodeType='dc2.large',
        MasterUsername=cluster_user,
        MasterUserPassword=cluster_password,
        # ClusterSecurityGroups=["default"],
        VpcSecurityGroupIds=["sg-0451e739676e3d587"],
        ClusterSubnetGroupName='default',
        AvailabilityZone='us-east-1a',
        PreferredMaintenanceWindow='',
        ClusterParameterGroupName='default.redshift-1.0',
        AutomatedSnapshotRetentionPeriod=1,
        ManualSnapshotRetentionPeriod=30,
        Port=5439,
        ClusterVersion='',
        AllowVersionUpgrade=False,
        NumberOfNodes=1,
        PubliclyAccessible=True,
        Encrypted=False

        # # HsmClientCertificateIdentifier='None',
        # # HsmConfigurationIdentifier='None',
        # # ElasticIp='',
        # Tags=[
        #     # {
        #     #     'Key': 'string',
        #     #     'Value': 'string'
        #     # },
        # ],
        # # KmsKeyId='',
        # EnhancedVpcRouting=False,
        # # AdditionalInfo='',
        # IamRoles=[
            
        # ],
        # MaintenanceTrackName='',
        # SnapshotScheduleIdentifier='',
        # AvailabilityZoneRelocation=False,
        # AquaConfigurationStatus='auto',
        # DefaultIamRoleArn='',
        # LoadSampleData=''

    )
    #return of response is Dict need to convert to list
    # ClusterIdentifier = response['Clusters'][0]['ClusterIdentifier']
    # ClusterEndpoint = response['Clusters'][0]['Endpoint']['Address']

    return  ClusterIdentifier


# cannot create LabRole is not allow to access to Redshift