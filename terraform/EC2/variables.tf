variable "region" {
    description = "The AWS region to deploy to"
    type = string
    default = "NA west"
}

variable "instance_tag_name" {
    description = "The Name tag for the EC2 instance"
    type = string
    default = "Flugel"
}

variable "instance_tag_owner" {
    description = "The Owner tag for the EC2 instance"
    type = string 
    default = "InfraTeam"
}