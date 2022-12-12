import boto3

from settings import * #aws_access_key_id , aws_secret_access_key , aws_session_token

redshift = boto3.client('redshift',

                    region_name='us-east-1',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token)

response = redshift.create_cluster(
    DBName='petclinic',
    ClusterIdentifier='redshift-cluster-petclinic',
    ClusterType='multi-node',
    NodeType='dc2.large',
    MasterUsername=cluster_user,
    MasterUserPassword=cluster_password,
    ClusterSecurityGroups=[
        'string',
    ],
    VpcSecurityGroupIds=[
        'string',
    ],
    ClusterSubnetGroupName='string',
    AvailabilityZone='string',
    PreferredMaintenanceWindow='string',
    ClusterParameterGroupName='string',
    AutomatedSnapshotRetentionPeriod=123,
    ManualSnapshotRetentionPeriod=123,
    Port=5439,
    ClusterVersion='string',
    AllowVersionUpgrade=False,
    NumberOfNodes=2,
    PubliclyAccessible=True,
    Encrypted=False,
    HsmClientCertificateIdentifier='string',
    HsmConfigurationIdentifier='string',
    ElasticIp='string',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    KmsKeyId='string',
    EnhancedVpcRouting=False,
    AdditionalInfo='string',
    IamRoles=[
        
    ],
    MaintenanceTrackName='string',
    SnapshotScheduleIdentifier='string',
    AvailabilityZoneRelocation=False,
    AquaConfigurationStatus='auto',
    DefaultIamRoleArn='string',
    LoadSampleData='string'
)

# cannot create LabRole is not allow to access to Redshift