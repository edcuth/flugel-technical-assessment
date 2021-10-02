variable "region" {
    description = "The AWS region to deploy to"
    type = string
    default = "NA west"
}

variable "bucket_tag_name" {
    description = "The Name tag set for the S3 Bucket"
    type = string
    default = "Flugel"
}

variable "bucket_tag_owner" {
    description = "Owner of the S3 bucket"
    type = string 
    default = "InfraTeam"
}