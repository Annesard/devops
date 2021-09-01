#Define keys and region
provider "aws" {
  access_key = "AKIAWDJJ5TLU3LKUEGPI"
  secret_key = "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"
  region     = "us-east-2"
}
#Define ec2 instance
resource "aws_instance" "instance1" {
  ami           = "ami-00399ec92321828f5"
  instance_type = "t2.micro"
  tags = {
    Name = "ubuntu-20.04"
  }
}