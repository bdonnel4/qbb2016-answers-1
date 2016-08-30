#!/usr/bin/env python

import sys

count=0

for line in sys.stdin:
    if line.startswith( "@" ):
        continue
    elif count<10:
        fields = line.rstrip( "\r\n").split( "\t" )
        print fields[2]
        count += 1