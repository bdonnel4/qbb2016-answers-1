#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    fields = line.rstrip( "\r\n").split( "\t" )
    if line.startswith( "@" ):
        continue
    elif fields[2] == "2L" and int(fields[3]) >= 10000 and int(fields[3]) <= 20000:
        count += 1
    else:
        continue
        
print "number of reads that start their alignment on chromosome 2L between base 10000 and 20000: ", count