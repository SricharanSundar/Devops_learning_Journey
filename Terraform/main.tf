provider "aws" {
  region     = "us-west-2"  # Change to your desired region
  access_key = "AKIAYS2NVN65WML7AU7Y"
  secret_key = "E7mH+Lma6dcxluNO5MlBcxY8NtkRw2dYlkjyoZIh"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"  # Change to a valid AMI ID in your region
  instance_type = "t2.micro"

  tags = {
    Name = "terraform-example"
  }
}
