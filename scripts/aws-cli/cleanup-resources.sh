#!/bin/bash
# Resource Cleanup Script

echo "🧹 Starting AWS resource cleanup..."

# List and terminate EC2 instances
echo "Checking for EC2 instances..."
aws ec2 describe-instances --query 'Reservations[*].Instances[*].InstanceId' --output text

# List S3 buckets
echo "Checking for S3 buckets..."
aws s3 ls

echo "⚠️  Please manually review and delete resources to avoid charges"
echo "📖 See cleanup instructions in each lab"
