#!/usr/bin/env python3
"""
Quiz Generator for AWS CLF-C02 Study Guide
Generates practice questions and quizzes
"""

import json
import random
from datetime import datetime

class QuizGenerator:
    def __init__(self):
        self.questions = []
        self.load_question_bank()
    
    def load_question_bank(self):
        """Load questions from question bank."""
        # This would load from a questions database or file
        self.questions = [
            {
                "id": 1,
                "question": "Which of the following best describes the AWS Shared Responsibility Model?",
                "options": [
                    "AWS is responsible for all security aspects",
                    "Customers are responsible for all security",
                    "AWS secures the cloud infrastructure while customers secure their data",
                    "Security is equally divided"
                ],
                "correct": 2,
                "explanation": "The shared responsibility model divides security responsibilities...",
                "topic": "Security",
                "difficulty": "easy"
            }
        ]
    
    def generate_quiz(self, num_questions=10, topic=None, difficulty=None):
        """Generate a quiz with specified parameters."""
        filtered_questions = self.questions
        
        if topic:
            filtered_questions = [q for q in filtered_questions if q.get('topic') == topic]
        
        if difficulty:
            filtered_questions = [q for q in filtered_questions if q.get('difficulty') == difficulty]
        
        selected_questions = random.sample(filtered_questions, min(num_questions, len(filtered_questions)))
        
        quiz_data = {
            "title": f"Practice Quiz - {datetime.now().strftime('%Y-%m-%d')}",
            "questions": selected_questions,
            "generated_at": datetime.now().isoformat(),
            "parameters": {
                "num_questions": num_questions,
                "topic": topic,
                "difficulty": difficulty
            }
        }
        
        return quiz_data
    
    def save_quiz(self, quiz_data, filename):
        """Save quiz to file."""
        with open(filename, 'w') as f:
            json.dump(quiz_data, f, indent=2)
        print(f"📝 Quiz saved to {filename}")
    
    def format_quiz_markdown(self, quiz_data):
        """Format quiz as markdown."""
        markdown = f"# {quiz_data['title']}

"
        
        for i, question in enumerate(quiz_data['questions'], 1):
            markdown += f"## Question {i}

"
            markdown += f"{question['question']}

"
            
            for j, option in enumerate(question['options']):
                letter = chr(65 + j)  # A, B, C, D
                markdown += f"**{letter})** {option}
"
            
            markdown += "
"
        
        return markdown

if __name__ == "__main__":
    generator = QuizGenerator()
    quiz = generator.generate_quiz(num_questions=5)
    markdown = generator.format_quiz_markdown(quiz)
    print(markdown)
