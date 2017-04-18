import boto3

elastic_load_balancer_client = boto3.client('elb')

elastic_load_balancer = elastic_load_balancer_client.create_load_balancer(
    LoadBalancerName='My-ELB',
    Listeners=[
        {
            'Protocol': 'HTTP',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'HTTP',
            'InstancePort': 80,
        #    'SSLCertificateId': 'string'
        },
    ],
    AvailabilityZones=[
        'us-east-1a',
    ],
    Subnets=[
        'subnet-593a272f',
    ],
    SecurityGroups=[
        'sg-3edf0f41',
    ],
    Scheme='internal'|'internet-facing',
    Tags=[
        {
            'Key': 'Name',
            'Value': 'My-ELB'
        },
    ]
)

elastic_load_balancer_health_check = elastic_load_balancer_client.configure_health_check(
    LoadBalancerName=elastic_load_balancer['LoadBalancerName'],
    HealthCheck={
        'Target': 'Tcp:22',
        'Interval': 10,
        'Timeout': 5,
        'UnhealthyThreshold': 5,
        'HealthyThreshold': 5
    }
)
