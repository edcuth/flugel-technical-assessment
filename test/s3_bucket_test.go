package test

import (
	"testing"

	"github.com/gruntwork-io/terratest/modules/aws"
	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/stretchr/testify/assert"
)

// Check if the tags of the S3 Buckets match the expected ones
func TestTerraformAwsS3Tags(t *testing.T) {
	t.Parallel()

	// Expected Name tag
	expectedName := "Fugel"

	// Expected Owner Tag
	expectedOwner := "InfraTeam"

	// Pick a random AWS region to test in. This helps ensure your code works in all regions.
	awsRegion := aws.GetRandomStableRegion(t, nil, nil)

	// Construct the terraform options with default retryable errors to handle the most common retryable errors in
	// terraform testing.
	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
		// The path to where our Terraform code is located
		TerraformDir: "./terraform/s3/",

		// Variables to pass to our Terraform code using -var options
		Vars: map[string]interface{}{
			"tag_bucket_name":  expectedName,
			"tag_bucket_Owner": expectedOwner,
			"region":           awsRegion,
		},
	})

	// At the end of the test, run `terraform destroy` to clean up any resources that were created
	defer terraform.Destroy(t, terraformOptions)

	// This will run `terraform init` and `terraform apply` and fail the test if there are any errors
	terraform.InitAndApply(t, terraformOptions)

	// Get the values of the tags from the Output
	bucketNameTag := terraform.Output(t, terraformOptions, "bucket_tag_name")
	bucketOwnerTag := terraform.Output(t, terraformOptions, "bucket_tag_owner")

	// Test if the values returned through the output match the expected values
	assert.Equal(t, bucketNameTag, expectedName)
	assert.Equal(t, bucketOwnerTag, expectedOwner)

}
