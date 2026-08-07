variable "aws_region" {
  default     = "eu-central-1"
  description = "AWS Region"
}

variable "instance_type" {
  default     = "t2.micro"
  description = "AWS EC2 Instance Type"
}

variable "key_name" {
  default     = "my-ssh-key"
  description = "Name of existing SSH Key Pair in AWS"
}