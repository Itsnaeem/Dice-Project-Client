resource "aws_instance" "server" {
  ami                    = "ami-0f5daaa3a7fb3378b"
  instance_type          = "t2.micro"
  subnet_id              = "subnet-0513fd176fd782647"
  vpc_security_group_ids = ["sg-0ed89c4f337f33716"]
  key_name               = "dice-project-ec2" # Add this line

  tags = {
    Name = "ClientInstance"
  }
}
