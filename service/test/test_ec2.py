import pytest

from ec2 import MyEC2Client

""" These tests use the moto library to mock an EC2 instance object, and then run
    all the needed tests locally. """

@pytest.fixture
def ec2_test(ec2_client):
    # Sets up a mock EC2 Instance with the ImageId, InstanceType, and Tags.
    ec2_client.run_instances(
        ImageId = "ami-0d5d9d301c853a04a", InstanceType ='t2.nano',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags':[{'Key':'Name', 'Value':'Fugel'}, {'Key':'Owner', 'Value':'InfraTeam'}]}],
        MaxCount=1,
        MinCount=1
        )
    yield


def test_instance_name_tag(ec2_client, ec2_test):
    # Check if the Name tag is set properly
    my_instance = MyEC2Client()
    tags = my_instance.list_tags()
    assert "Name" in tags[0] and "Fugel" in tags[1]

def test_instance_owner_tag(ec2_client, ec2_test):
    # Check if the Owner tag is set properly
    my_instance = MyEC2Client()
    tags = my_instance.list_tags()
    assert "Owner" in tags[0] and "InfraTeam" in tags[1]

def test_shutdown_instance(ec2_client, ec2_test):
    # Check if the instance is stopped properly by calling the stop_instance() method
    # then check the response object returned by the method to corroborate it's been stopped properly.
    my_instance = MyEC2Client()
    response = my_instance.shutdown()
    assert response['StoppingInstances'][0]['CurrentState']['Name'] in ["shutting-down", "stopped", "stopping"]

