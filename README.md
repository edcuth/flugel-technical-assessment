# fugel-technical-assessment
### Technical challenge as requested by the Fugel Team


## Challenge:
 1.   Create Terraform code to create an S3 bucket and an EC2 instance. Both resources must be tagged with Name=Flugel, Owner=InfraTeam.
 2.   Using Terratest, create the test automation for the Terraform code,validating that both resources are tagged properly.
 3.   In the EC2 instance, run a simple HTTP service written in Python with two endpoints:
 4.   /tags: must display EC2 instance tags.
 5.   /shutdown: must shutdown the instance.
 6.   Setup Github Actions to run a pipeline to validate this code.
 7.   Publish your code in a public GitHub repository, and share a Pull Request with your code. Do not merge into master until the PR is approved.
 8.   Include documentation describing the steps to run and test the automation.


## Documentation:
Hi, I'm the Documentation for this repo, but people call me Doc, and I'm here to (hopefully) answer all your questions and help you get this repo up and running!

### Terraform
#### S3 Bucket
The S3 Bucket Terraform code is in the S3 folder. The main.tf file will inizialize a S3 Bucket, using variables.tf. Output.tf is used for testing.


#### EC2 Instance
The EC2 Instance Terraform code is ubicated in the EC2 folder, the main.tf will initialize an EC2 Instance using variables.tf. Output.tf is used for testing.

### Testing
For automated testing for both the S3 bucket and the EC2 instance:
1. Sign up for AWS.
2. Configure your AWS credentials using a supported method for AWS CLI tool, suck as setting the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables.
3. Install Terraform and make sure it is on your PATH.
4. Install Golang and make sure this code is checked out into your GOPATH.
5. cd test
6. go test -v -run ec2_test or go test -v -run ec_bucket_test
7. The tests will check if both the EC2 instance and the S3 Bucket have the correct tags

### Python HTTP service
To be updated!

### Endpoints
#### /tags
This endpoint will return the tags of the EC2 instance and the S3 Cluster, being in this case:
* Name=Flugel
* Owner=InfraTeam

#### /shutdown
This endpoint will stop the instance, without hibernating it, by calling the stop_instance method from the boto3 library.

### Github Actions
To be updated!



