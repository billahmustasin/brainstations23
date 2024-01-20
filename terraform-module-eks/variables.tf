variable "region" {
 description = "AWS region"
 default     = "us-east-1"
}

variable "name" {
 description = "Name for the resources"
 default     = "ascode-cluster"
}

variable "vpc_cidr" {
 description = "CIDR block for the VPC"
 default     = "10.123.0.0/16"
}

variable "azs" {
 description = "Availability zones"
 default     = ["us-east-1a", "us-east-1b"]
}

variable "public_subnets" {
 description = "Public subnets"
 default     = ["10.123.1.0/24", "10.123.2.0/24"]
}

variable "private_subnets" {
 description = "Private subnets"
 default     = ["10.123.3.0/24", "10.123.4.0/24"]
}

variable "intra_subnets" {
 description = "Intra subnets"
 default     = ["10.123.5.0/24", "10.123.6.0/24"]
}