package test

import (
	"testing"

	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/stretchr/testify/assert"
)

func TestTerraformAwsHelloWorldExample(t *testing.T) {
	t.Parallel()

	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
		// The path to where our Terraform code is located
		TerraformDir: "../EC2/main.tf",
	})

	// `terraform destroy` to clean up any resources that were created.
	defer terraform.Destroy(t, terraformOptions)

	// Run `terraform init` and `terraform apply`. Fail the test if there are any errors.
	terraform.InitAndApply(t, terraformOptions)

	// Expected tag values for `Name` and `Onwer`
	expectedName := "Flugel"
	expectedOwner := "InfraTeam"

	// Get the values of the tags from the Output
	instanceNameTag := terraform.Output(t, terraformOptions, "instance_tag_name")
	instanceOwnerTag := terraform.Output(t, terraformOptions, "instance_tag_owner")

	// Test if the values returned through the output match the expected values
	assert.Equal(t, instanceNameTag, expectedName)
	assert.Equal(t, instanceOwnerTag, expectedOwner)

}
