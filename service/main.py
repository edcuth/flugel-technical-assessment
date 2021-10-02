from flask import Flask
import boto3

def create_app():
    app = Flask(__name__)
    ec2 = boto3.client('ec2')
    
    @app.route('/tags')
    def tags():
        # Returns the tags of the EC2 Instance.
        response = ec2.describe_tags(InstanceIds=['aws_instance.fugel_assessment'])
        tags = ""
        for r in response['Tags']:
            tags += r['key'] + ": " + r['value'] + "\n"
        return tags

    @app.route('/shutdown')
    def shutdown():
        # Stops the instance. 
        ec2.stop_instances(InstanceIds=['aws_instance.fugel_assessment'])

    return app


if __name__ == '__main__':
    create_app()