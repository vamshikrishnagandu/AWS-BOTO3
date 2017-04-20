import boto3

elasticbeanstalk_client = boto3.client('elasticbeanstalk')

elasticbeanstalk_application = elasticbeanstalk_client.create_application(
    ApplicationName='My-Application',
    Description='Sample web application'
 )

elasticbeanstalk_environment = elasticbeanstalk_client.create_environment(
    ApplicationName=elasticbeanstalk_application['ApplicationName'],
    EnvironmentName='My-Environment',
    CNAMEPrefix='My-App',
    VersionLabel='v1',
    SolutionStackName='64bit Amazon Linux 2016.09 v2.0.2 running Packer 0.12.1'
)

elasticbeanstalk_application_version = elasticbeanstalk_client.create_application_version(
    ApplicationName=elasticbeanstalk_application['ApplicationName'],
    VersionLabel=elasticbeanstalk_environment['VersionLabel'],
    SourceBundle={
        'S3Bucket': 'my-bucket',
        'S3Key': 'sample.war'
    },
    AutoCreateApplication=True,
    Process=True
)
