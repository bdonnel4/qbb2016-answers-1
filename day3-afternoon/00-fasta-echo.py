#!/usr/bin/env python

"""
Parse every FASTA record from stdin and print each
"""

import sys
import fasta

# What I want:

reader = FASTAReader(sys.stdin)

# while 1:
#     identifier, sequence = reader.next()
#     if identifier is None:
#         break
#     print identifier, sequence

for identifier, sequence in reader:
    print identifier, sequence