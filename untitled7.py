# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 02:07:36 2024

@author: ralph
"""


names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Option to input search term
search_term = input("Enter a name to search for: ")


if search_term in names:
    print(f"{search_term} is in the list.")
else:
    print(f"{search_term} is not in the list.")
