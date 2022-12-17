import pickle
from datetime import datetime

response = {
    'Marker': 'string',
    'Clusters': [
        {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'VpcEndpoints': [
                    {
                        'VpcEndpointId': 'string',
                        'VpcId': 'string',
                        'NetworkInterfaces': [
                            {
                                'NetworkInterfaceId': 'string',
                                'SubnetId': 'string',
                                'PrivateIpAddress': 'string',
                                'AvailabilityZone': 'string'
                            },
                        ]
                    },
                ]
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
            'ClusterSecurityGroups': [
                {
                    'ClusterSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'ClusterParameterGroups': [
                {
                    'ParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'ClusterParameterStatusList': [
                        {
                            'ParameterName': 'string',
                            'ParameterApplyStatus': 'string',
                            'ParameterApplyErrorDescription': 'string'
                        },
                    ]
                },
            ],
            'ClusterSubnetGroupName': 'string',
            'VpcId': 'string',
            'AvailabilityZone': 'string',
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'MasterUserPassword': 'string',
                'NodeType': 'string',
                'NumberOfNodes': 123,
                'ClusterType': 'string',
                'ClusterVersion': 'string',
                'AutomatedSnapshotRetentionPeriod': 123,
                'ClusterIdentifier': 'string',
                'PubliclyAccessible': True|False,
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
            },
            'ClusterVersion': 'string',
            'AllowVersionUpgrade': True|False,
            'NumberOfNodes': 123,
            'PubliclyAccessible': True|False,
            'Encrypted': True|False,
            'RestoreStatus': {
                'Status': 'string',
                'CurrentRestoreRateInMegaBytesPerSecond': 123.0,
                'SnapshotSizeInMegaBytes': 123,
                'ProgressInMegaBytes': 123,
                'ElapsedTimeInSeconds': 123,
                'EstimatedTimeToCompletionInSeconds': 123
            },
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
                'SnapshotCopyGrantName': 'string'
            },
            'ClusterPublicKey': 'string',
            'ClusterNodes': [
                {
                    'NodeRole': 'string',
                    'PrivateIPAddress': 'string',
                    'PublicIPAddress': 'string'
                },
            ],
            'ElasticIpStatus': {
                'ElasticIp': 'string',
                'Status': 'string'
            },
            'ClusterRevisionNumber': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'KmsKeyId': 'string',
            'EnhancedVpcRouting': True|False,
            'IamRoles': [
                {
                    'IamRoleArn': 'string',
                    'ApplyStatus': 'string'
                },
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            },
            'AvailabilityZoneRelocationStatus': 'string',
            'ClusterNamespaceArn': 'string',
            'TotalStorageCapacityInMegaBytes': 123,
            'AquaConfiguration': {
                'AquaStatus': 'applying',
                'AquaConfigurationStatus': 'auto'
            },
            'DefaultIamRoleArn': 'string',
            'ReservedNodeExchangeStatus': {
                'ReservedNodeExchangeRequestId': 'string',
                'Status': 'RFAILED',
                'RequestTime': datetime(2015, 1, 1),
                'SourceReservedNodeId': 'string',
                'SourceReservedNodeType': 'string',
                'SourceReservedNodeCount': 123,
                'TargetReservedNodeOfferingId': 'string',
                'TargetReservedNodeType': 'string',
                'TargetReservedNodeCount': 123
            }
        },
    ]
}

# import json

# result = str(response)
# x = result.replace("\'", "\"")

# print(x)


# y = json.loads(x)
print(type(response))
print(response.keys())
print(response['Clusters'][0])
print(type(response['Clusters'][0]))
print(len(response['Clusters'][0]))
print(response['Clusters'][0].keys())
print(response['Clusters'][0]['ClusterIdentifier'])
print(response['Clusters'][0]['Endpoint'].keys())
print(response['Clusters'][0]['Endpoint']['Address'])