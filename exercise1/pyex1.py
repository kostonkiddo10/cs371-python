# Davian Albarran | s1302682 | CS-371
# pyex1.py - Standard input in Python

import sys

for line in sys.stdin:
    # Using sys.stdout.write because it does not add extra newline like print.
    sys.stdout.write(line)
    line = line.rstrip()
    sys.stdout.write(str(len(line)) + "\n")
