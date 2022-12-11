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
    ClusterType='single-node',
    NodeType='dc2.large',
    MasterUsername='awsuser',
    MasterUserPassword=MasterUserPassword,
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
    Port=123,
    ClusterVersion='string',
    AllowVersionUpgrade=True|False,
    NumberOfNodes=1,
    PubliclyAccessible=False,
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
        'arn:aws:iam::423544405765:role/myRedshiftRole',
    ],
    MaintenanceTrackName='string',
    SnapshotScheduleIdentifier='string',
    AvailabilityZoneRelocation=False,
    AquaConfigurationStatus='auto',
    DefaultIamRoleArn='string',
    LoadSampleData='string'
)

# cannot create LabRole is not allow to access to Redshift