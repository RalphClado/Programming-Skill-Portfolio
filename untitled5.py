# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 01:59:34 2024

@author: ralph
"""

# Define the correct password
correct_password = "Ralph is pogi"
# Set the maximum number of attempts
max_attempts = 5
# Initialize attempt counter
attempts = 0

# Start the password entry loop
while attempts < max_attempts:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect password. You have {remaining_attempts} attempt(s) left.")
        
# If maximum attempts are reached
if attempts == max_attempts:
    print("Maximum attempts reached. Authorities have been alerted.")
