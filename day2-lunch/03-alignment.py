#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    if "NH:i:1" in line:
        count += 1
            
print "number of number of reads that map to exactly one location in the genome", count