# Davian Albarran | CS-371 | Spring 2024
# pyex3.py - Read roster.txt fields into a dictionary.
import re

input_file = open('roster.txt', 'r')

roster = {} # Declare empty dict

for student in input_file:
    [last, first, email] = re.split(r"\s*,\s*", student)
    
    id = re.sub('@monmouth.edu\n', '', email)

    roster[id] = last + ", " + first

for id in roster.keys():
    print(id + ', ' + roster[id])
