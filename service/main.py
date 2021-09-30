from flask import Flask
import boto3

def create_app():
    app = Flask(__name__)
    ec2 = boto3.client('ec2')
    
    @app.route('/tags')
    def tags():
        response = ec2.describe_tags(InstanceIds=['aws_instance.fugel_assessment'])
        tags = ""
        for key in response.keys():
            tags += key + ": " + response[key] + "\n"
        return tags

    @app.route('/shutdown')
    def shutdown():
        ec2.stop_instance(Hibernate=False, InstanceIds=['aws_instance.fugel_assessment'])

    return app