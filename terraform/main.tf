provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "jenkins" {
  ami           = "ami-04b4f1a9cf54c11d0" # Amazon Linux 2 AMI
  instance_type = "t2.micro"
  tags = {
    Name = "Jenkins-Server"
  }
}

resource "aws_db_instance" "mysql" {
  allocated_storage    = 10
  engine               = "mysql"
  instance_class       = "db.t3.micro"
  engine_version       = "8.0"
  db_name              = "mydb"
  username             = "admin"
  password             = "password"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
}

