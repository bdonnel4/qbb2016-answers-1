#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""

import sys

line = sys.stdin.readline()
# verify header line starts with >
assert line.startswith(">")
# extract id - whole line
## identifier = line[1:].rstrip("\n\r")
# extract id - space (after the carrot sign, before the space)
identifier = line[1:].split()[0]

# list to store sequence
sequences = []

# loop forever (no condidtion)
while 1:
    line = sys.stdin.readline().rstrip("\r\n")
    if line.startswith(">") or line == "":
        break
    else:
        sequences.append(line)
        
print identifier, "".join(sequences)