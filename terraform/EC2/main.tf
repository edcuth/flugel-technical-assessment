provider "aws" {
  region = var.region
}

resource "aws_instance" "fugel_assessment" {
  
  ami                    = "ami-0d5d9d301c853a04a"
  instance_type          = "t2.micro"

  tags = {
    Name = var.instance_tag_name
    Owner = var.instance_tag_owner
  }

  provisioner "file "{
    source = "../../service"
    destination = "/"
  }

  user_data = <<EOF
  #!/bin/bash
  cd service
  pip install -r requirements.txt
  python main.py
  EOF
}

resource "aws_security_group" "instance" {
  ingress {
    from_port = 8080
    to_port = 8080
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
