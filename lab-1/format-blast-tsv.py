#!/usr/bin/env python

import sys

blast = open(sys.argv[1])

for line in blast:
    fields = line.rstrip( "\r\n").split( "\t" )
    fields[3] = fields[3].translate(None,'-')
    length = int(fields[2]) - int(fields[1])
    length = int(length)
    if length == 10292:
        print ">"+ fields[0]+ "\n"+ fields[3]
    