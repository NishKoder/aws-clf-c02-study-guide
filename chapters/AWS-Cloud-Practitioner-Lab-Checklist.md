# 🧪 AWS Cloud Practitioner - Hands-On Lab Checklist

> **Filename:** `AWS-Cloud-Practitioner-Lab-Checklist.md`  
> **Purpose:** Complete laboratory reference for AWS Cloud Practitioner certification preparation  
> **Total Labs:** 28 hands-on exercises across 10 chapters  
> **Free Tier Compatible:** 86% of labs  

---

## 📚 Table of Contents

- [Chapter 1: Introduction to Cloud Computing & AWS](#chapter-1-introduction-to-cloud-computing--aws)
- [Chapter 2: AWS Global Infrastructure](#chapter-2-aws-global-infrastructure)
- [Chapter 3: Identity and Access Management (IAM)](#chapter-3-identity-and-access-management-iam)
- [Chapter 4: Compute Services](#chapter-4-compute-services)
- [Chapter 5: Storage Services](#chapter-5-storage-services)
- [Chapter 6: Database Services](#chapter-6-database-services)
- [Chapter 7: Networking Services](#chapter-7-networking-services)
- [Chapter 8: Security and Compliance](#chapter-8-security-and-compliance)
- [Chapter 9: Monitoring and Management](#chapter-9-monitoring-and-management)
- [Chapter 10: Pricing and Support](#chapter-10-pricing-and-support)
- [Lab Summary Statistics](#-lab-summary-statistics)
- [Prerequisites](#-prerequisites-for-all-labs)
- [Getting Started](#-getting-started)

---

## Chapter 1: Introduction to Cloud Computing & AWS

### Lab 1.1: Creating Your First AWS Account
- **📋 Description:** Step-by-step AWS account creation and initial setup
- **🔧 AWS Services:** AWS Account Management, IAM
- **📖 Chapter Reference:** Chapter 1, Section 1.4
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 15 minutes
- **🎯 Learning Objectives:**
  - Create and verify AWS account
  - Understand billing dashboard basics
  - Set up initial security configurations

### Lab 1.2: Exploring the AWS Management Console
- **📋 Description:** Navigate and customize the AWS Management Console interface
- **🔧 AWS Services:** AWS Management Console, Dashboard
- **📖 Chapter Reference:** Chapter 1, Section 1.5
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 20 minutes
- **🎯 Learning Objectives:**
  - Master console navigation
  - Customize dashboard widgets
  - Understand service categorization

---

## Chapter 2: AWS Global Infrastructure

### Lab 2.1: Exploring AWS Regions and Availability Zones
- **📋 Description:** Investigate global infrastructure components and regional services
- **🔧 AWS Services:** EC2, CloudFormation
- **📖 Chapter Reference:** Chapter 2, Section 2.3
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 30 minutes
- **🎯 Learning Objectives:**
  - Compare regional service availability
  - Understand latency implications
  - Explore AZ characteristics

### Lab 2.2: Understanding Edge Locations with CloudFront
- **📋 Description:** Deploy content distribution and analyze edge location performance
- **🔧 AWS Services:** CloudFront, S3
- **📖 Chapter Reference:** Chapter 2, Section 2.4
- **💰 Free Tier:** ✅ Yes (12 months)
- **⏱️ Duration:** 45 minutes
- **🎯 Learning Objectives:**
  - Configure CloudFront distribution
  - Measure performance improvements
  - Understand caching behaviors

---

## Chapter 3: Identity and Access Management (IAM)

### Lab 3.1: Creating IAM Users and Groups
- **📋 Description:** Establish user management hierarchy with groups and permissions
- **🔧 AWS Services:** IAM
- **📖 Chapter Reference:** Chapter 3, Section 3.2
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 25 minutes
- **🎯 Learning Objectives:**
  - Create users with programmatic access
  - Organize users into logical groups
  - Apply principle of least privilege

### Lab 3.2: Implementing IAM Policies and Roles
- **📋 Description:** Design custom policies and cross-service roles
- **🔧 AWS Services:** IAM, EC2
- **📖 Chapter Reference:** Chapter 3, Section 3.3
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 40 minutes
- **🎯 Learning Objectives:**
  - Write custom JSON policies
  - Create and assign service roles
  - Test policy effectiveness

### Lab 3.3: Multi-Factor Authentication (MFA) Setup
- **📋 Description:** Enhance account security with MFA implementation
- **🔧 AWS Services:** IAM
- **📖 Chapter Reference:** Chapter 3, Section 3.4
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 15 minutes
- **🎯 Learning Objectives:**
  - Configure virtual MFA devices
  - Test MFA login process
  - Understand security benefits

---

## Chapter 4: Compute Services

### Lab 4.1: Launching Your First EC2 Instance
- **📋 Description:** Deploy and configure a basic Amazon EC2 virtual machine
- **🔧 AWS Services:** EC2, Security Groups
- **📖 Chapter Reference:** Chapter 4, Section 2
- **💰 Free Tier:** ✅ Yes (750 hours/month)
- **⏱️ Duration:** 35 minutes
- **🎯 Learning Objectives:**
  - Launch t2.micro instance
  - Configure security groups
  - Connect via SSH/RDP

### Lab 4.2: Working with EC2 Instance Types and Storage
- **📋 Description:** Compare instance families and attach additional storage
- **🔧 AWS Services:** EC2, EBS
- **📖 Chapter Reference:** Chapter 4, Section 4.3
- **💰 Free Tier:** ✅ Yes (30 GB EBS)
- **⏱️ Duration:** 45 minutes
- **🎯 Learning Objectives:**
  - Compare instance type performance
  - Attach and mount EBS volumes
  - Understand storage options

### Lab 4.3: Introduction to AWS Lambda
- **📋 Description:** Create serverless functions with event-driven triggers
- **🔧 AWS Services:** Lambda, CloudWatch
- **📖 Chapter Reference:** Chapter 4, Section 4.4
- **💰 Free Tier:** ✅ Yes (1M requests/month)
- **⏱️ Duration:** 30 minutes
- **🎯 Learning Objectives:**
  - Write basic Lambda functions
  - Configure event triggers
  - Monitor function execution

### Lab 4.4: Container Basics with AWS Fargate
- **📋 Description:** Deploy containerized applications without server management
- **🔧 AWS Services:** ECS, Fargate
- **📖 Chapter Reference:** Chapter 4, Section 4.5
- **💰 Free Tier:** ❌ No (minimal charges apply)
- **⏱️ Duration:** 50 minutes
- **🎯 Learning Objectives:**
  - Create container definitions
  - Deploy with Fargate
  - Understand serverless containers

---

## Chapter 5: Storage Services

### Lab 5.1: Creating and Managing S3 Buckets
- **📋 Description:** Implement object storage with versioning and access controls
- **🔧 AWS Services:** S3
- **📖 Chapter Reference:** Chapter 5, Section 5.2
- **💰 Free Tier:** ✅ Yes (5 GB storage)
- **⏱️ Duration:** 30 minutes
- **🎯 Learning Objectives:**
  - Create buckets with proper naming
  - Configure bucket policies
  - Enable versioning and logging

### Lab 5.2: S3 Storage Classes and Lifecycle Policies
- **📋 Description:** Optimize costs through intelligent storage class transitions
- **🔧 AWS Services:** S3, S3 Glacier
- **📖 Chapter Reference:** Chapter 5, Section 5.3
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 40 minutes
- **🎯 Learning Objectives:**
  - Configure lifecycle policies
  - Compare storage class costs
  - Implement archival strategies

### Lab 5.3: EBS Volume Management
- **📋 Description:** Manage block storage with snapshots and encryption
- **🔧 AWS Services:** EC2, EBS
- **📖 Chapter Reference:** Chapter 5, Section 5.4
- **💰 Free Tier:** ✅ Yes (30 GB)
- **⏱️ Duration:** 35 minutes
- **🎯 Learning Objectives:**
  - Create and attach EBS volumes
  - Perform snapshot operations
  - Enable encryption at rest

### Lab 5.4: AWS EFS File System Setup
- **📋 Description:** Deploy shared file systems across multiple instances
- **🔧 AWS Services:** EFS, EC2
- **📖 Chapter Reference:** Chapter 5, Section 5.5
- **💰 Free Tier:** ✅ Yes (5 GB)
- **⏱️ Duration:** 45 minutes
- **🎯 Learning Objectives:**
  - Create EFS file systems
  - Mount across multiple instances
  - Configure performance modes

---

## Chapter 6: Database Services

### Lab 6.1: Creating an Amazon RDS Database
- **📋 Description:** Deploy managed relational databases with automated backups
- **🔧 AWS Services:** RDS (MySQL)
- **📖 Chapter Reference:** Chapter 6, Section 6.2
- **💰 Free Tier:** ✅ Yes (750 hours db.t2.micro)
- **⏱️ Duration:** 40 minutes
- **🎯 Learning Objectives:**
  - Launch RDS MySQL instance
  - Configure security groups
  - Test database connectivity

### Lab 6.2: DynamoDB Table Operations
- **📋 Description:** Work with NoSQL databases and perform CRUD operations
- **🔧 AWS Services:** DynamoDB
- **📖 Chapter Reference:** Chapter 6, Section 6.3
- **💰 Free Tier:** ✅ Yes (25 GB storage)
- **⏱️ Duration:** 35 minutes
- **🎯 Learning Objectives:**
  - Create DynamoDB tables
  - Perform read/write operations
  - Configure global secondary indexes

### Lab 6.3: Database Migration with AWS DMS
- **📋 Description:** Migrate data between different database engines
- **🔧 AWS Services:** DMS, RDS, S3
- **📖 Chapter Reference:** Chapter 6, Section 6.4
- **💰 Free Tier:** ❌ No (minimal charges)
- **⏱️ Duration:** 60 minutes
- **🎯 Learning Objectives:**
  - Set up migration endpoints
  - Configure replication tasks
  - Monitor migration progress

---

## Chapter 7: Networking Services

### Lab 7.1: Building a Custom VPC
- **📋 Description:** Design and implement isolated network environments
- **🔧 AWS Services:** VPC, Subnets, Route Tables
- **📖 Chapter Reference:** Chapter 7, Section 7.2
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 50 minutes
- **🎯 Learning Objectives:**
  - Create VPC with CIDR blocks
  - Configure public/private subnets
  - Set up internet and NAT gateways

### Lab 7.2: Configuring Security Groups and NACLs
- **📋 Description:** Implement layered network security controls
- **🔧 AWS Services:** VPC, EC2, Security Groups
- **📖 Chapter Reference:** Chapter 7, Section 7.3
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 40 minutes
- **🎯 Learning Objectives:**
  - Configure stateful security groups
  - Implement stateless NACLs
  - Test security rule effectiveness

### Lab 7.3: Load Balancing with Application Load Balancer
- **📋 Description:** Distribute traffic across multiple EC2 instances
- **🔧 AWS Services:** ELB, EC2, Auto Scaling
- **📖 Chapter Reference:** Chapter 7, Section 7.4
- **💰 Free Tier:** ✅ Yes (750 hours)
- **⏱️ Duration:** 55 minutes
- **🎯 Learning Objectives:**
  - Configure Application Load Balancer
  - Set up health checks
  - Implement auto scaling policies

### Lab 7.4: Content Delivery with CloudFront
- **📋 Description:** Accelerate content delivery through global edge locations
- **🔧 AWS Services:** CloudFront, S3, Route 53
- **📖 Chapter Reference:** Chapter 7, Section 7.5
- **💰 Free Tier:** ✅ Yes (50 GB data transfer)
- **⏱️ Duration:** 45 minutes
- **🎯 Learning Objectives:**
  - Create CloudFront distributions
  - Configure caching behaviors
  - Measure performance improvements

---

## Chapter 8: Security and Compliance

### Lab 8.1: AWS CloudTrail Configuration
- **📋 Description:** Enable comprehensive API logging and audit trails
- **🔧 AWS Services:** CloudTrail, S3, CloudWatch
- **📖 Chapter Reference:** Chapter 8, Section 8.2
- **💰 Free Tier:** ✅ Yes (one trail free)
- **⏱️ Duration:** 30 minutes
- **🎯 Learning Objectives:**
  - Configure CloudTrail logging
  - Analyze API call events
  - Set up log file validation

### Lab 8.2: Data Encryption with AWS KMS
- **📋 Description:** Implement encryption for data at rest and in transit
- **🔧 AWS Services:** KMS, S3, EBS
- **📖 Chapter Reference:** Chapter 8, Section 8.3
- **💰 Free Tier:** ✅ Yes (20,000 requests)
- **⏱️ Duration:** 40 minutes
- **🎯 Learning Objectives:**
  - Create customer-managed keys
  - Encrypt S3 objects and EBS volumes
  - Manage key rotation policies

### Lab 8.3: AWS Config for Compliance Monitoring
- **📋 Description:** Monitor resource configurations for compliance violations
- **🔧 AWS Services:** Config, S3
- **📖 Chapter Reference:** Chapter 8, Section 8.4
- **💰 Free Tier:** ❌ No (charges apply)
- **⏱️ Duration:** 45 minutes
- **🎯 Learning Objectives:**
  - Enable Config recording
  - Create compliance rules
  - Review configuration history

### Lab 8.4: Security Assessment with Inspector
- **📋 Description:** Automated security assessments of EC2 instances
- **🔧 AWS Services:** Inspector, EC2
- **📖 Chapter Reference:** Chapter 8, Section 8.5
- **💰 Free Tier:** ✅ Yes (90 days trial)
- **⏱️ Duration:** 35 minutes
- **🎯 Learning Objectives:**
  - Install Inspector agents
  - Run security assessments
  - Analyze vulnerability findings

---

## Chapter 9: Monitoring and Management

### Lab 9.1: CloudWatch Metrics and Alarms
- **📋 Description:** Monitor resource performance and set up automated alerts
- **🔧 AWS Services:** CloudWatch, EC2, SNS
- **📖 Chapter Reference:** Chapter 9, Section 9.2
- **💰 Free Tier:** ✅ Yes (10 alarms)
- **⏱️ Duration:** 35 minutes
- **🎯 Learning Objectives:**
  - Create custom metrics
  - Configure alarm thresholds
  - Set up SNS notifications

### Lab 9.2: Centralized Logging with CloudWatch Logs
- **📋 Description:** Aggregate and analyze application logs from multiple sources
- **🔧 AWS Services:** CloudWatch Logs, EC2, Lambda
- **📖 Chapter Reference:** Chapter 9, Section 9.3
- **💰 Free Tier:** ✅ Yes (5 GB ingestion)
- **⏱️ Duration:** 40 minutes
- **🎯 Learning Objectives:**
  - Stream logs to CloudWatch
  - Create log groups and streams
  - Set up log retention policies

### Lab 9.3: Infrastructure as Code with CloudFormation
- **📋 Description:** Deploy and manage resources using JSON/YAML templates
- **🔧 AWS Services:** CloudFormation, EC2, S3
- **📖 Chapter Reference:** Chapter 9, Section 9.4
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 50 minutes
- **🎯 Learning Objectives:**
  - Write CloudFormation templates
  - Deploy stacks with parameters
  - Update and delete resources

### Lab 9.4: Systems Manager for Instance Management
- **📋 Description:** Manage EC2 instances at scale without SSH access
- **🔧 AWS Services:** Systems Manager, EC2
- **📖 Chapter Reference:** Chapter 9, Section 9.5
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 45 minutes
- **🎯 Learning Objectives:**
  - Use Session Manager for access
  - Apply patches with Patch Manager
  - Run commands across instances

---

## Chapter 10: Pricing and Support

### Lab 10.1: AWS Cost Calculator and Budgets
- **📋 Description:** Estimate costs and set up budget monitoring
- **🔧 AWS Services:** Cost Explorer, Budgets, Billing
- **📖 Chapter Reference:** Chapter 10, Section 10.2
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 25 minutes
- **🎯 Learning Objectives:**
  - Use AWS Pricing Calculator
  - Create cost budgets
  - Set up billing alerts

### Lab 10.2: Cost Optimization with Trusted Advisor
- **📋 Description:** Identify opportunities for cost savings and optimization
- **🔧 AWS Services:** Trusted Advisor, Support
- **📖 Chapter Reference:** Chapter 10, Section 10.3
- **💰 Free Tier:** ✅ Yes (basic checks)
- **⏱️ Duration:** 30 minutes
- **🎯 Learning Objectives:**
  - Review Trusted Advisor recommendations
  - Understand cost optimization strategies
  - Implement suggested improvements

### Lab 10.3: Resource Tagging for Cost Management
- **📋 Description:** Organize and track resource costs using tags
- **🔧 AWS Services:** EC2, S3, Cost Explorer
- **📖 Chapter Reference:** Chapter 10, Section 10.4
- **💰 Free Tier:** ✅ Yes
- **⏱️ Duration:** 35 minutes
- **🎯 Learning Objectives:**
  - Implement tagging strategies
  - Track costs by tags
  - Create cost allocation reports

---

## 📊 Lab Summary Statistics

| **Category** | **Details** |
|--------------|-------------|
| **Total Labs** | 28 comprehensive hands-on exercises |
| **Free Tier Compatible** | 24 labs (86% of total) |
| **Non-Free Tier Labs** | 4 labs (minimal charges < $5 total) |
| **Total Estimated Time** | ~17 hours of hands-on practice |
| **Average Lab Duration** | 38 minutes per lab |
| **AWS Services Covered** | 25+ core AWS services |
| **Skill Levels** | Beginner to Intermediate |

### Free Tier Usage Breakdown
- **Always Free:** 18 labs (64%)
- **12-Month Free:** 6 labs (21%)
- **Minimal Cost:** 4 labs (14%)

### Time Investment by Chapter
| Chapter | Labs | Duration | Complexity |
|---------|------|----------|------------|
| Ch 1-2 | 4 labs | 110 min | Beginner |
| Ch 3-5 | 9 labs | 330 min | Beginner-Intermediate |
| Ch 6-8 | 9 labs | 395 min | Intermediate |
| Ch 9-10 | 6 labs | 225 min | Intermediate |

---

## 🎯 Prerequisites for All Labs

### Required Setup
- **AWS Account:** Active account with administrative privileges
- **Billing:** Credit card on file (for identity verification)
- **Browser:** Modern web browser (Chrome, Firefox, Safari, Edge)
- **Internet:** Stable broadband connection
- **Email:** Access to email for AWS notifications

### Recommended Tools
- **AWS CLI:** Command-line interface installed and configured
- **Text Editor:** VS Code, Sublime Text, or similar
- **SSH Client:** PuTTY (Windows) or Terminal (Mac/Linux)
- **JSON Validator:** For CloudFormation templates
- **Note-taking App:** For documenting lab results

### Knowledge Prerequisites
- Basic understanding of cloud computing concepts
- Familiarity with IP networking fundamentals
- Basic command-line experience (helpful but not required)
- Understanding of JSON/YAML formats (for advanced labs)

### Security Best Practices
- Enable MFA on root account immediately
- Create IAM user for daily operations
- Never share access keys or credentials
- Use least privilege principle for permissions
- Regularly review and rotate access keys

---

## 🚀 Getting Started

### Step 1: Account Preparation
1. **Create AWS Account** following Lab 1.1
2. **Set up billing alerts** to monitor spending
3. **Enable MFA** on root account
4. **Create IAM user** for lab exercises
5. **Bookmark AWS Console** for quick access

### Step 2: Lab Environment Setup
1. **Choose your primary region** (us-east-1 recommended for beginners)
2. **Create dedicated lab folder** for screenshots and notes
3. **Set up AWS CLI** with your IAM user credentials
4. **Join study community** forums for support
5. **Schedule regular practice** sessions (2-3 labs per week recommended)

### Step 3: Lab Execution Strategy
1. **Read entire lab** before starting
2. **Follow sequential order** within each chapter
3. **Take screenshots** of key configurations
4. **Document any errors** and troubleshooting steps
5. **Clean up resources** immediately after each lab

### Step 4: Progress Tracking
- [ ] **Chapter 1:** Cloud Computing Basics (2 labs)
- [ ] **Chapter 2:** Global Infrastructure (2 labs)
- [ ] **Chapter 3:** IAM Fundamentals (3 labs)
- [ ] **Chapter 4:** Compute Services (4 labs)
- [ ] **Chapter 5:** Storage Solutions (4 labs)
- [ ] **Chapter 6:** Database Services (3 labs)
- [ ] **Chapter 7:** Networking (4 labs)
- [ ] **Chapter 8:** Security & Compliance (4 labs)
- [ ] **Chapter 9:** Monitoring & Management (4 labs)
- [ ] **Chapter 10:** Pricing & Support (3 labs)

---

## 🔧 Troubleshooting & Support

### Common Issues
- **Insufficient Permissions:** Verify IAM policies and roles
- **Region Availability:** Ensure services are available in your region
- **Free Tier Limits:** Monitor usage to avoid unexpected charges
- **Resource Dependencies:** Follow lab sequence for proper setup
- **Network Connectivity:** Check security groups and NACLs

### Getting Help
- **AWS Documentation:** https://docs.aws.amazon.com
- **AWS Forums:** https://forums.aws.amazon.com
- **AWS Support:** Available through console (Basic plan included)
- **Community Resources:** Reddit r/aws, Stack Overflow
- **YouTube Channels:** AWS official and certified trainers

### Cost Management
- **Set up billing alerts** before starting
- **Use AWS Budgets** to track spending
- **Clean up resources** after each lab
- **Review charges** weekly during lab period
- **Contact support** if unexpected charges occur

---

## 📋 Lab Completion Checklist

After completing each lab:
- [ ] **Screenshot key configurations** for your portfolio
- [ ] **Document lessons learned** and key takeaways
- [ ] **Clean up all resources** to avoid ongoing charges
- [ ] **Update progress tracker** and mark lab complete
- [ ] **Review related exam topics** in study guide
- [ ] **Schedule next lab session** to maintain momentum

---

## 🏆 Certification Preparation Tips

### Exam Readiness Indicators
- [ ] Completed all 28 hands-on labs
- [ ] Can explain each AWS service's primary use case
- [ ] Understand pricing models for core services
- [ ] Familiar with AWS global infrastructure
- [ ] Know security best practices and compliance basics

### Final Study Phase
1. **Review lab notes** and screenshots
2. **Take practice exams** to identify weak areas
3. **Schedule certification exam** when consistently scoring 80%+
4. **Continue hands-on practice** with real-world scenarios
5. **Join exam study groups** for peer support

---

## 📞 Contact & Resources

- **GitHub Repository:** [Link to full eBook repository]
- **Author Support:** [Contact information]
- **Study Group:** [Community forum link]
- **Updates:** Check repository for lab updates and corrections
- **Feedback:** Submit issues and suggestions via GitHub

---

*Happy learning, and best of luck with your AWS Cloud Practitioner certification journey! 🚀*

**Last Updated:** July 2025  
**Version:** 1.0  
**License:** MIT