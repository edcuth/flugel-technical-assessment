variable "region" {
    description = "The AWS region to deploy to"
    type = string
    default = "NA west"
}

variable "tag_bucket_name" {
    description = "The Name tag set for the S3 Bucket"
    type = string
    default = "Fugel"
}

variable "tag_bucket_owner" {
    description = "Owner of the S3 bucket"
    type = string 
    default = "InfraTeam"
}