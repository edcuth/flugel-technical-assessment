import boto3   


class MyEC2Client:
    def __init__(self, region_name='us-east-1'):
        self.client = boto3.client("ec2", region_name=region_name)
    
    def list_tags(self):
        """ Returns a dict of tag keys:values. """
        response = self.client.describe_tags()
        k = []
        v = []
        for tag in response['Tags']:
            k.append(tag['Key'])
            v.append(tag['Value'])
        return [k, v]

    def shutdown(self):
        instances = self.client.describe_instances()
        instanceIds = [name['InstanceId'] for name in instances['Reservations'][0]['Instances']]
        return self.client.stop_instances(InstanceIds=instanceIds)