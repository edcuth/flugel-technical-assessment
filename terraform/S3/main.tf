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
        Nanme = var.tag_bucket_name
        Owner = var.tag_bucket_owner
    }
}

