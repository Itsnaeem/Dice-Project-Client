resource "aws_instance" "client" {
  ami           = "ami-0a91cd140a1fc148a" # Ensure this is the latest Ubuntu AMI for us-east-2
  instance_type = "t2.micro"
  subnet_id     = "subnet-027c4dd4becc64d43" # Choose another appropriate subnet
  vpc_security_group_ids = ["sg-0ed89c4f337f33716"] # Default VPC security group

  tags = {
    Name = "ClientInstance"
  }
}
