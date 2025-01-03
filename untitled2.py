# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 01:47:19 2024

@author: ralph
"""

# Get user input
name = input("Please enter your name (first and last): ")
hometown = input("Please enter your hometown: ")
age_input = input("Please enter your age: ")

# Store the information in a dictionary
user_info = {
    "name": name,
    "hometown": hometown,
    "age": age_input
}

# Print the values on separate lines
print("\n".join(user_info.values()))

# Check if age is a number
try:
    age = int(age_input)
except ValueError:
    print("Invalid age input. Please enter a valid integer for age.")
