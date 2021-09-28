provider "aws" {
  region = "${var.region}"
}

resource "aws_ec2_instance" "fugel_assessment" {
  
  ami                    = "ami-0d5d9d301c853a04a"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.instance.id]

  user_data = <<EOF
  #!/bin/bash
  
}