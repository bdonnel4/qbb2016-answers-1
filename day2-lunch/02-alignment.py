#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    if "NM:i:0" in line:
        count += 1
            
print "number of perfect alignments to genome", count

