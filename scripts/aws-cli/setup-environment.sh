#!/bin/bash
# AWS CLI Setup Script for Study Guide

echo "🚀 Setting up AWS CLI for CLF-C02 Study Guide..."

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "❌ AWS CLI not found. Please install it first:"
    echo "   - Linux: sudo apt install awscli"
    echo "   - macOS: brew install awscli" 
    echo "   - Windows: Download from https://aws.amazon.com/cli/"
    exit 1
fi

echo "✅ AWS CLI found: $(aws --version)"

# Configure AWS CLI
echo "📝 Configuring AWS CLI..."
echo "Please enter your AWS credentials:"
aws configure

echo "🔍 Testing AWS connection..."
aws sts get-caller-identity

echo "✅ AWS CLI setup complete!"
