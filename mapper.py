#!/usr/bin/env python3
import sys
import re

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    words = re.findall(r'\b\w+\b', line)
    # count the word
    for word in words:
        print(f'{word.lower()}\t1')
