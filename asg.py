import boto3

autoscaling_client = boto3.client('autoscaling')

launch_configuration = autoscaling_client.create_launch_configuration(
    LaunchConfigurationName='My-LC',
    ImageId='ami-b63769a1',
    KeyName='my-keyName',
    SecurityGroups=[
        'sg-3edf0f41',
    ],

    #UserData='string',

    InstanceType='t2.micro',
    BlockDeviceMappings=[
        {
            'VirtualName': 'EBS',
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'SnapshotId': 'snap-b9a222c1',
                'VolumeSize': 10,
                'VolumeType': 'io1',
                'DeleteOnTermination': True,
                'Iops': 500,
                'Encrypted': True
            },
            'NoDevice': True
        },
    ],
    InstanceMonitoring={
        'Enabled': False
    },

    IamInstanceProfile='My-IAM-Role',
    EbsOptimized=True
    #AssociatePublicIpAddress=True|False,
    #PlacementTenancy='string'
)

auto_scaling_group = autoscaling_client.create_auto_scaling_group(
    AutoScalingGroupName='My-ASG',
    LaunchConfigurationName=launch_configuration['LaunchConfigurationName'],
    MinSize=1,
    MaxSize=2,
    DesiredCapacity=1,
    DefaultCooldown=300,
    Subnets=[
        'subnet-593a272f','subnet-5b1c3303'
    ],
    AvailabilityZones=[
        'us-east-1a','us-east-1b'
    ],
    LoadBalancerNames=[
        'My-ELB',
    ],
    #TargetGroupARNs=[
        'string',
    ],
    HealthCheckType='EC2',
    HealthCheckGracePeriod=60,
    TerminationPolicies=[
        'string',
    ],
    NewInstancesProtectedFromScaleIn=True,
    Tags=[
        {
            'ResourceId': 'My-ASG',
            'ResourceType': 'auto-scaling-group',
            'Key': 'Name',
            'Value': 'My-ASG',
            'PropagateAtLaunch': True
        },
    ]
)
