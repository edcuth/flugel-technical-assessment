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
Hi, I'm the Documentation for this repo, but that name is kinda long, so people call me Doc, and I'm here to (hopefully) answer all your questions and help you get this repo up and running!

### Terraform
#### S3 Bucket
Our S3 Bucket is created using our main.tf ubicated in the /terraform/S3 directory.

#### S3 Bucket Test
To be updated!

#### EC2 Instance
To be updated!

#### EC2 Instance Test
To be updated!

### Python HTTP service
To be updated!

### Endpoints
#### /tags
This endpoint will return the tags of the EC2 instance and the S3 Cluster, being in this case:
* Name=Flugel
* Owner=InfraTeam

#### /shutdown


### Github Actions
To be updated!



