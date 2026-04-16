terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # Configuración del estado remoto
  backend "s3" {
    bucket = "state-terraform-counter" # Cámbialo por uno real
    key    = "serverless-visitor/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = "us-east-1" # La región que prefieras
}