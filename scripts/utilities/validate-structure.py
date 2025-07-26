#!/usr/bin/env python3
"""
Repository Structure Validator
Validates that all required files and directories exist
"""

import os
import sys
from pathlib import Path

class StructureValidator:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.errors = []
        self.warnings = []
    
    def validate_directories(self):
        """Validate required directories exist."""
        required_dirs = [
            "chapters", "labs", "practice-tests", "scenarios",
            "resources", "images", "scripts", "docs", ".github"
        ]
        
        for directory in required_dirs:
            if not (self.base_path / directory).exists():
                self.errors.append(f"Missing required directory: {directory}")
    
    def validate_files(self):
        """Validate required files exist."""
        required_files = [
            "README.md", "LICENSE", "CONTRIBUTING.md", 
            "CODE_OF_CONDUCT.md", ".gitignore"
        ]
        
        for filename in required_files:
            if not (self.base_path / filename).exists():
                self.errors.append(f"Missing required file: {filename}")
    
    def validate_chapters(self):
        """Validate chapter files exist."""
        chapter_dir = self.base_path / "chapters"
        if chapter_dir.exists():
            expected_chapters = [
                "chapter-01-aws-cloud-overview.md",
                "chapter-02-core-services.md",
                "chapter-03-security-compliance.md",
                "chapter-04-pricing-billing.md",
                "chapter-05-support-architecture.md"
            ]
            
            for chapter in expected_chapters:
                if not (chapter_dir / chapter).exists():
                    self.warnings.append(f"Chapter file not found: {chapter}")
    
    def run_validation(self):
        """Run all validations."""
        print("🔍 Validating repository structure...")
        
        self.validate_directories()
        self.validate_files()
        self.validate_chapters()
        
        # Report results
        if self.errors:
            print("❌ Validation failed with errors:")
            for error in self.errors:
                print(f"   - {error}")
            return False
        
        if self.warnings:
            print("⚠️  Validation passed with warnings:")
            for warning in self.warnings:
                print(f"   - {warning}")
        
        print("✅ Repository structure validation complete!")
        return True

if __name__ == "__main__":
    validator = StructureValidator()
    success = validator.run_validation()
    sys.exit(0 if success else 1)
