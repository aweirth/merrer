#!/usr/bin/env python3
import sys
import re

# Read input line by line
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Extract words using a regular expression
    words = re.findall(r'\b\w+\b', line)
    # Emit the word and a count of 1
    for word in words:
        print(f'{word.lower()}\t1')
