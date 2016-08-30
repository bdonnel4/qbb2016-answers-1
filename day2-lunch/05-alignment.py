#!/usr/bin/env python

import sys

count = 0

# find number of alignments
for line in sys.stdin:
    if line.startswith( "@" ):
        continue
    else:
        count += 1
        
float_count = float(count)

MAPQ_sum = 0
sys.stdin.seek(0)
# find sum of MAPQ
for line in sys.stdin:
    if line.startswith( "@" ):
        continue
    else:
        fields = line.rstrip( "\r\n").split( "\t" )
        MAPQ_sum += int(fields[4])
        
float_MAPQ_sum = float(MAPQ_sum)

# calculate average MAPQ score
avg = float_MAPQ_sum/float_count
print "Average MAPq score: ", avg
        