# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 01:54:39 2024

@author: ralph
"""

# Define a dictionary with the number of days in each month
days_in_month = {
    1: 31,  # January
    2: 28,  # February (normal year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Function to get the number of days in a month
def get_days_in_month(month):
    if month == 2:  # February
        year = input("Is it a leap year? (yes/no): ").strip().lower()
        if year == "yes":
            return 29  # Leap year
        else:
            return 28  # Normal year
    else: 
        return days_in_month.get(month)

# Main program
try:
    month_number = int(input("Enter the month number (1-12): "))
    if 1 <= month_number <= 12:
        days = get_days_in_month(month_number)
        print(f"There are {days} days in month {month_number}.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter a valid integer for the month number.")
