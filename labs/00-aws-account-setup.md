# Lab: AWS Free Tier Account Setup

## Overview
**Objective**: aws free tier account setup  
**Estimated Time**: 30-45 minutes  
**Cost**: Free Tier eligible  
**Prerequisites**: AWS account with admin access

## Learning Objectives
By completing this lab, you will:
- [ ] Understand the key concepts
- [ ] Gain hands-on experience
- [ ] Apply best practices
- [ ] Prepare for exam scenarios

## Lab Instructions

### Step 1: Preparation
1. Sign in to your AWS Management Console
2. Ensure you're in the correct region
3. Verify Free Tier status

### Step 2: Implementation
*Detailed steps coming soon...*

### Step 3: Verification
*Verification steps coming soon...*

### Step 4: Cleanup
⚠️ **Important**: Always clean up resources to avoid charges
*Cleanup steps coming soon...*

## Troubleshooting
*Common issues and solutions coming soon...*

## Additional Resources
- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Free Tier](https://aws.amazon.com/free/)

---
*This lab is part of the [AWS CLF-C02 Study Guide](../README.md)*
# Lab 01: AWS Account Setup and Console Navigation

## Overview
**Objective**: Set up AWS Free Tier account, navigate the AWS Management Console, and explore core AWS services (EC2, S3, IAM)  
**Estimated Time**: 120-180 minutes  
**Cost**: Free Tier eligible  
**Prerequisites**: Valid email address, credit card for account verification, and basic understanding of web browsers

## Learning Objectives
By completing this lab, you will:
- [ ] Successfully create and configure an AWS Free Tier account
- [ ] Navigate the AWS Management Console effectively
- [ ] Explore EC2, S3, and IAM service dashboards
- [ ] Install and configure AWS CLI for programmatic access
- [ ] Execute basic AWS CLI commands to interact with services
- [ ] Understand AWS console security and access management

## Lab Instructions

### Step 1: AWS Free Tier Account Creation

#### 1.1 Navigate to AWS Sign-up
1. Open your web browser and go to `https://aws.amazon.com`
2. Click the **"Create an AWS Account"** button in the top-right corner
3. You'll be redirected to the account creation page

#### 1.2 Provide Account Information
1. Enter your email address in the **"Email address"** field
2. Create a strong password with the following requirements:
   - Minimum 8 characters
   - Include uppercase letters, lowercase letters, numbers, and symbols
   - Example: `MyAWS2025!Study`
3. Confirm your password
4. Enter an AWS account name (can be your name or organization name)
5. Click **"Continue"**

> **💡 Security Tip**: Use a password manager to generate and store a strong, unique password

#### 1.3 Contact Information
1. Select your account type:
   - Choose **"Personal"** for individual learning purposes
   - Choose **"Professional"** if using for business
2. Fill in all required contact information:
   - Full name (as it appears on your credit card)
   - Phone number (required for verification)
   - Complete address information
3. Read and accept the AWS Customer Agreement
4. Click **"Create Account and Continue"**

#### 1.4 Payment Information
1. Enter your credit card or debit card information
   - Card number
   - Expiration date
   - Security code (CVV)
   - Cardholder name
2. Billing address (if different from contact address)
3. Set up automatic payments (recommended for convenience)
4. Click **"Verify and Continue"**

> **⚠️ Important**: This card is for account verification. Free Tier services won't incur charges, but always monitor your usage

#### 1.5 Identity Verification
1. AWS will initiate an automated call or send an SMS to your provided phone number
2. Answer the call or check your SMS for a 4-digit verification code
3. Enter the verification code when prompted on the website
4. Click **"Continue"** after successful verification

#### 1.6 Support Plan Selection
1. Choose **"Basic Support - Free"** for learning purposes
2. Review the support plan features:
   - Customer Service & Communities access
   - Documentation and whitepapers
   - Support forums
3. Click **"Complete Sign Up"**

#### 1.7 Account Activation Confirmation
1. You'll receive a confirmation email at your registered address
2. Account activation typically takes 2-10 minutes
3. Once activated, you'll see a success message: "Congratulations! Your AWS account is ready"

### Step 2: First Login and Console Familiarization

#### 2.1 Access the AWS Management Console
1. Navigate to `https://console.aws.amazon.com`
2. Click **"Sign In to the Console"**
3. Select **"Root user"** (you'll create IAM users later)
4. Enter your email address and password
5. Complete any additional MFA prompts if configured
6. Click **"Sign In"**

#### 2.2 Console Overview and Navigation
Familiarize yourself with the console layout:

**Main Navigation Elements:**
- **AWS Services Menu**: Top-left, provides access to all AWS services
- **Region Selector**: Top-right, shows current AWS Region (e.g., us-east-1)
- **Account Menu**: Top-right dropdown with your account information
- **Search Bar**: Center-top, for quickly finding services
- **Recently Visited Services**: Quick access to frequently used services

#### 2.3 Set Your Default Region
1. Click the Region dropdown in the top-right corner
2. Select an appropriate Region for your location:
   - **US East (N. Virginia) - us-east-1**: Most services, lowest cost (recommended for learning)
   - **US West (Oregon) - us-west-2**: West Coast users
   - **Europe (Ireland) - eu-west-1**: European users
   - **Asia Pacific (Sydney) - ap-southeast-2**: Asia-Pacific users
3. Note: Some services are global (like IAM), others are region-specific

> **📝 Note**: We recommend us-east-1 for this lab as it has the most services available and often the lowest pricing

### Step 3: Exploring Amazon EC2

#### 3.1 Navigate to EC2 Service
1. In the AWS Services menu, search for **"EC2"**
2. Click on **"EC2"** under the Compute category
3. You'll arrive at the EC2 Dashboard

#### 3.2 EC2 Dashboard Exploration
Review the dashboard sections:

**Resources Summary:**
- Running Instances: 0 (initially)
- Volumes: 0
- Key Pairs: 0
- Security Groups: 1 (default)

**Service Health:**
- Check the current status of EC2 services in your region

**Account Attributes:**
- Instance limits (typically 20 On-Demand instances for new accounts)
- vCPU limits (typically 64 vCPUs)

#### 3.3 Explore Launch Instance Wizard (Without Creating)
1. Click the **"Launch Instance"** button
2. Explore each section without actually launching:

**Name and Tags:**
- Instance name: `my-first-instance-exploration`
- Tags: Key=Environment, Value=Learning

**Application and OS Images (AMI):**
- Amazon Linux 2023 AMI (Free tier eligible)
- Ubuntu Server 22.04 LTS (Free tier eligible)
- Windows Server 2022 Base (Free tier eligible)

**Instance Type:**
- t3.micro (1 vCPU, 1 GB RAM) - Free tier eligible ✅
- t3.small (1 vCPU, 2 GB RAM) - Not free tier
- t3.medium (2 vCPU, 4 GB RAM) - Not free tier

**Key Pair (Login):**
- Create new key pair option
- Existing key pair selection
- Proceed without key pair (not recommended)

3. **Important**: Click **"Cancel"** at the bottom to exit without launching an instance

#### 3.4 Explore EC2 Features in Left Navigation
Navigate through the left sidebar:

**Instances:**
- Instances: View and manage EC2 instances
- Instance Types: Compare different instance specifications
- Launch Templates: Predefined instance configurations

**Images:**
- AMIs: Amazon Machine Images
- Snapshots: EBS volume snapshots

**Elastic Block Store:**
- Volumes: EBS storage volumes
- Snapshots: Volume backups

**Network & Security:**
- Security Groups: Virtual firewalls
- Key Pairs: SSH key management
- Elastic IPs: Static IP addresses

### Step 4: Exploring Amazon S3

#### 4.1 Navigate to S3 Service
1. Use the Services menu to search for **"S3"**
2. Click on **"Amazon S3"** under Storage
3. You'll arrive at the S3 Console

#### 4.2 S3 Console Overview
The S3 Console displays:

**Main Areas:**
- **Buckets**: Container list (initially empty)
- **General Purpose Buckets**: Standard S3 buckets
- **Directory Buckets**: S3 Express One Zone buckets
- **Access Points**: Advanced access management

#### 4.3 Create a Test Bucket (Optional Exercise)
1. Click **"Create bucket"**
2. **Bucket Configuration:**
   - Bucket name: `your-initials-clf-c02-test-bucket-2025` (must be globally unique)
   - AWS Region: Select your current region
   - Object Ownership: ACLs disabled (recommended)
   - Block Public Access: Keep all settings enabled (recommended)
   - Bucket Versioning: Disable (for this lab)
   - Default encryption: Server-side encryption with Amazon S3 managed keys (SSE-S3)
3. Review settings and click **"Create bucket"**

> **⚠️ Cost Note**: Empty S3 buckets don't incur charges, but uploaded objects count against Free Tier limits

#### 4.4 Explore Bucket Features (If Created)
If you created a bucket, click on it to explore:

**Objects Tab:**
- Upload files interface
- Folder creation
- Object management

**Properties Tab:**
- Bucket versioning
- Static website hosting
- Event notifications
- Transfer acceleration

**Permissions Tab:**
- Bucket policy
- Access control lists (ACLs)
- Cross-origin resource sharing (CORS)

**Metrics Tab:**
- Request metrics
- Storage analytics

### Step 5: Exploring AWS IAM

#### 5.1 Navigate to IAM Service
1. Search for **"IAM"** in the Services menu
2. Click on **"Identity and Access Management (IAM)"**
3. Note: IAM is a global service (no region selection needed)

#### 5.2 IAM Dashboard Overview
Review the dashboard components:

**Security Recommendations:**
- ⚠️ Add MFA to your root user account
- ⚠️ Create individual IAM users
- ⚠️ Use groups to assign permissions to IAM users
- ⚠️ Apply an IAM password policy

**Quick Links:**
- Create individual IAM users
- Manage MFA
- Create group
- Create role

**Access Management Summary:**
- Users: 0 (initially)
- Groups: 0
- Roles: Service-linked roles may exist
- Policies: AWS managed policies available

#### 5.3 Explore IAM Users
1. Click **"Users"** in the left navigation panel
2. You'll see an empty users list (root user doesn't appear here)
3. Click **"Create user"** to explore the creation process:

**User Details:**
- User name field
- AWS Management Console access option
- Programmatic access considerations

**Permissions Options:**
- Add user to group
- Copy permissions from existing user
- Attach policies directly

4. **Important**: Click **"Cancel"** to exit without creating a user

#### 5.4 Explore IAM Policies
1. Click **"Policies"** in the left navigation
2. Browse AWS managed policies (hundreds available)
3. Use the filter to search for specific policies:
   - Search: `AmazonS3ReadOnlyAccess`
   - Search: `AmazonEC2ReadOnlyAccess`
   - Search: `PowerUserAccess`

4. Click on **"AmazonS3ReadOnlyAccess"** to view:
   - Policy summary
   - JSON policy document
   - Services and access levels
   - Resources affected

#### 5.5 Review Security Recommendations
Return to the IAM Dashboard and note the security recommendations:
- ✅ Enable MFA for root user (we'll address this in security labs)
- ✅ Create individual IAM users (best practice for daily operations)
- ✅ Use groups to assign permissions (easier management)
- ✅ Apply least privilege principle (minimal necessary permissions)

### Step 6: AWS CLI Installation and Configuration

#### 6.1 Install AWS CLI

**For Windows:**
1. Download the AWS CLI MSI installer from `https://aws.amazon.com/cli/`
2. Run the downloaded installer (`AWSCLIV2.msi`)
3. Follow the installation wizard prompts
4. Open Command Prompt and verify installation:
   ```cmd
   aws --version
   ```
   Expected output: `aws-cli/2.x.x Python/3.x.x Windows/...`

**For macOS:**
```bash
# Method 1: Using Homebrew (recommended)
brew install awscli

# Method 2: Using the installer
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

# Verify installation
aws --version
```

**For Linux (Ubuntu/Debian):**
```bash
# Method 1: Using package manager
sudo apt update
sudo apt install awscli

# Method 2: Using pip
pip3 install awscli

# Method 3: Using the installer (recommended for latest version)
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Verify installation
aws --version
```

#### 6.2 Create Access Keys for CLI Access
1. In the AWS Console, navigate to IAM
2. Click on your root user account name (top-right dropdown)
3. Select **"Security credentials"**
4. Scroll down to **"Access keys"** section
5. Click **"Create access key"**
6. Select **"Command Line Interface (CLI)"**
7. Acknowledge the alternatives recommendation
8. Optionally add a description tag: `CLF-C02-Study-CLI`
9. Click **"Create access key"**
10. **Important**: Download the CSV file or copy both keys immediately
    - Access Key ID: `AKIAIOSFODNN7EXAMPLE`
    - Secret Access Key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

> **🔒 Security Warning**: Never share these keys or commit them to version control

#### 6.3 Configure AWS CLI
1. Open terminal/command prompt
2. Run the configuration command:
   ```bash
   aws configure
   ```
3. Enter the following information when prompted:
   ```
   AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
   AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   Default region name [None]: us-east-1
   Default output format [None]: json
   ```

#### 6.4 Test AWS CLI Functionality
Execute these commands to verify CLI setup:

```bash
# Test 1: Verify your identity
aws sts get-caller-identity
```
Expected output:
```json
{
    "UserId": "123456789012",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:root"
}
```

```bash
# Test 2: List S3 buckets
aws s3 ls
```
Expected output:
```
2025-07-26 10:30:45 your-initials-clf-c02-test-bucket-2025
```

```bash
# Test 3: List EC2 instances
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType]' --output table
```
Expected output:
```
------------------
|DescribeInstances|
------------------
```

```bash
# Test 4: List IAM users
aws iam list-users --query 'Users[*].[UserName,CreateDate]' --output table
```

```bash
# Test 5: Get account summary
aws iam get-account-summary
```

### Step 7: Verification

#### 7.1 Account Verification Checklist
Verify your setup by checking the following:

- [ ] AWS account successfully created and activated
- [ ] Able to sign in to AWS Management Console
- [ ] Can navigate to EC2, S3, and IAM services
- [ ] Understand the layout of each service dashboard
- [ ] AWS CLI installed and configured
- [ ] CLI commands execute successfully and return expected results

#### 7.2 Knowledge Verification
Answer these questions to verify your understanding:

1. **What is the difference between AWS Regions and Availability Zones?**
2. **Why is the root user not recommended for daily AWS operations?**
3. **What are the main components of the EC2 service dashboard?**
4. **How do S3 bucket names need to be structured globally?**
5. **What information is required to configure the AWS CLI?**

### Step 8: Cleanup

⚠️ **Important**: Always clean up resources to avoid charges

#### 8.1 Remove Test S3 Bucket (If Created)
1. **Via AWS Console:**
   - Go to S3 console
   - Select your test bucket
   - Click **"Empty"** to remove all objects
   - Type the bucket name to confirm
   - Click **"Delete"** to remove the bucket
   - Type the bucket name again to confirm

2. **Via AWS CLI:**
   ```bash
   # Remove all objects from bucket
   aws s3 rm s3://your-initials-clf-c02-test-bucket-2025 --recursive
   
   # Delete the bucket
   aws s3 rb s3://your-initials-clf-c02-test-bucket-2025
   ```

#### 8.2 Secure Access Keys
1. **Rotate Access Keys (Recommended):**
   - Create new access keys
   - Update CLI configuration
   - Delete old access keys

2. **Or Delete Access Keys (If Not Needed):**
   - Go to IAM → Security credentials
   - Find your access key
   - Click **"Delete"**
   - Confirm deletion

#### 8.3 Review Free Tier Usage
1. Navigate to **Billing & Cost Management**
2. Click **"Free tier"** in the left navigation
3. Review current usage against limits:
   - EC2: 750 hours/month of t3.micro
   - S3: 5 GB of standard storage
   - Data transfer: 100 GB/month

## Troubleshooting

### Common Issues and Solutions

#### Account Creation Issues
**Problem**: Email verification not received
**Solution**: 
- Check spam/junk folders
- Ensure email address is typed correctly
- Contact AWS support if needed

**Problem**: Credit card verification fails
**Solution**:
- Verify card details are correct
- Ensure card is enabled for international transactions
- Try a different card if available
- Contact your bank if charges are blocked

#### Console Access Issues
**Problem**: Cannot sign in to console
**Solution**:
- Verify email and password are correct
- Check if account is fully activated
- Try password reset if needed
- Clear browser cache and cookies

**Problem**: Region-specific services not visible
**Solution**:
- Check selected region in top-right corner
- Switch to us-east-1 for maximum service availability
- Verify service is available in your selected region

#### CLI Configuration Issues
**Problem**: `aws` command not found
**Solution**:
- Verify AWS CLI installation
- Check system PATH environment variable
- Restart terminal after installation
- Reinstall AWS CLI if necessary

**Problem**: Access denied errors with CLI
**Solution**:
- Verify access keys are correct
- Check IAM permissions
- Ensure access keys are active
- Reconfigure with `aws configure`

**Problem**: CLI returns incorrect region data
**Solution**:
- Check default region in configuration
- Use `aws configure get region` to verify
- Specify region explicitly: `aws s3 ls --region us-east-1`

#### Service-Specific Issues
**Problem**: Cannot create S3 bucket
**Solution**:
- Ensure bucket name is globally unique
- Use lowercase letters, numbers, and hyphens only
- Avoid periods in bucket names
- Try a different name with timestamp

**Problem**: EC2 instance limits reached
**Solution**:
- Check current running instances
- Terminate unused instances
- Request limit increase if needed for legitimate use
- Use different instance types if available

## Additional Resources

### AWS Documentation
- [AWS Account Setup Guide](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)
- [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [Getting Started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [Getting Started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
- [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)

### Video Tutorials
- [AWS Console Overview](https://www.youtube.com/watch?v=Ul2FdY7jBJE)
- [AWS CLI Installation and Setup](https://www.youtube.com/watch?v=ZbgvF7yWoqA)

### Community Resources
- [AWS re:Post](https://repost.aws/) - Community Q&A
- [AWS Reddit Community](https://www.reddit.com/r/aws/)
- [AWS Stack Overflow](https://stackoverflow.com/questions/tagged/amazon-web-services)

### Cost Management
- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Billing and Cost Management Console](https://console.aws.amazon.com/billing/)

---

**Lab Complete! 🎉**

You have successfully completed the AWS Account Setup and Console Navigation lab. You now have:
- ✅ A fully configured AWS Free Tier account
- ✅ Hands-on experience with the AWS Management Console
- ✅ Familiarity with EC2, S3, and IAM services
- ✅ A working AWS CLI installation
- ✅ Understanding of basic AWS navigation and security concepts

**Next Steps:**
- Proceed to [Lab 02: EC2 Instance Management](../labs/02-ec2-instance-management.md)
- Review [Chapter 2: AWS Core Services](../chapters/chapter-02-core-services.md)
- Practice with additional AWS CLI commands

*This lab is part of the [AWS CLF-C02 Study Guide](../README.md)*