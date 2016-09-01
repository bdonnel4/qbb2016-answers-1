#!/usr/bin/env python

import sys

for line in sys.stdin:
    if line.startswith( "t_id" ):
        print line.rstrip( "\r\n" )
        continue
    #split fields on tab
    fields = line.rstrip( "\r\n").split( "\t" )
    #convert and compute length
    length = int( fields[4] ) - int( fields[3] )
    #write out with new field tab separated
    fields.append( str( length ) )
    # join fields back into a tab separated indexsl
    print "\t".join( fields )
    
    