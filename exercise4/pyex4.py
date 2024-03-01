# Davian Albarran | s1302682 | Spring CS-371
# pyex4.py - Search and replace multi-line student records

import re

# Apply read method immediately and store the entire contents in one string "input_roster
input_roster = open('cs176roster.webadvisor.txt', 'r',).read()

student_pattern = re.compile(r'.+, .+\n\d{7}')

students = student_pattern.findall(input_roster) # students is a list.

for student in students:
    student = student.replace("\n", ', s')
    print(student)
