terraform {

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket = "sctp-ce3-tfstate-bucket-1"
    key    = "friends-ce-3-group-capstone-infra.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = "us-west-2"
}
