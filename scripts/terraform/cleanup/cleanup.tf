# Cleanup script for lab resources
# This will destroy all resources created by the lab environment

terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# This file forces destruction of all resources
# Run with: terraform apply -auto-approve
# Then: terraform destroy -auto-approve

resource "null_resource" "cleanup_warning" {
  provisioner "local-exec" {
    command = "echo 'WARNING: This will destroy all lab resources. Press Ctrl+C to cancel, or wait 10 seconds to continue.'"
  }
  
  provisioner "local-exec" {
    command = "sleep 10"
  }
}
