provider "aws" {
 region = var.region
}

terraform {
  backend "s3" {
    bucket = "terrafrm-bs-state"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}