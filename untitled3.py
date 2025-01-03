# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 01:50:09 2024

@author: ralph
"""

# Define a dictionary with countries and their capitals
quiz_questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Portugal": "Lisbon"
}

# Function to conduct the quiz
def run_quiz(questions):
    for country, capital in questions.items():
        answer = input(f"What is the capital of {country}? ").strip()
        if answer.lower() == capital.lower():  # Ignore case
            print("Nice One!Correct!")
        else:
            print(f"Wrong! womp womp, answer is {capital}.")

# Start the quiz
run_quiz(quiz_questions)
