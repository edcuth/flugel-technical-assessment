provider "aws" {
    region = var.region
}

resource "aws_s3_bucket" "fugel_assessment" {
    bucket = "${local.aws_account_id}-${var.tag_bucket_name}"
    acl = "private"

    versioning = {
        enabled = true
    }

    tags = {
        Name = var.bucket_tag_name
        Owner = var.bucket_tag_owner
    }
}

