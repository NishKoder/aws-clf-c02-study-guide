#!/usr/bin/env python3
"""
Progress Tracker for AWS CLF-C02 Study Guide
"""

import json
import os
from datetime import datetime

class StudyProgressTracker:
    def __init__(self):
        self.progress_file = "study_progress.json"
        self.load_progress()
    
    def load_progress(self):
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                self.progress = json.load(f)
        else:
            self.progress = {
                "chapters": {},
                "labs": {},
                "quizzes": {},
                "start_date": str(datetime.now().date()),
                "total_study_hours": 0
            }
    
    def save_progress(self):
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def mark_chapter_complete(self, chapter_num):
        self.progress["chapters"][f"chapter_{chapter_num}"] = {
            "completed": True,
            "date": str(datetime.now().date())
        }
        self.save_progress()
        print(f"✅ Chapter {chapter_num} marked as complete!")
    
    def add_study_time(self, hours):
        self.progress["total_study_hours"] += hours
        self.save_progress()
        print(f"📚 Added {hours} study hours. Total: {self.progress['total_study_hours']}")
    
    def show_progress(self):
        print("📊 Study Progress Report")
        print("=" * 30)
        print(f"Start Date: {self.progress['start_date']}")
        print(f"Total Study Hours: {self.progress['total_study_hours']}")
        print(f"Chapters Completed: {len(self.progress['chapters'])}/5")
        print(f"Labs Completed: {len(self.progress['labs'])}")
        print(f"Quizzes Completed: {len(self.progress['quizzes'])}")

if __name__ == "__main__":
    tracker = StudyProgressTracker()
    tracker.show_progress()
