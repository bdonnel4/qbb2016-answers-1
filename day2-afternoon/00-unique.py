#!/usr/bin/env python

""""
Prints the unique gene names from a t_data.ctab file
commented out list version b/c took too long (~5 sec)
"""

import sys

#gene_names_seen = []
gene_names_seen = {} # dict()

for i, line in enumerate( sys.stdin ):
    #enumerate to skip first line
    if i == 0:
        continue
    fields = line.rstrip( "\n\r" ).split( "\t" )
    gene_name = fields[9]
    if gene_name not in gene_names_seen:
        # gene_names_seen.append( gene_name )
        #must equal to something, can be true,number; must map key to value
        # gene_names_seen[ gene_name ] =  True #dict
        # gene_names_seen.add( gene_name )
        gene_names_seen[ gene_name ] = 1
    else:
        gene_names_seen[ gene_name ] += 1

for gene_name in gene_names_seen:
    print gene_name, gene_names_seen[ gene_name ]

#for gene_name, count in gene_names_seen.iteritems():
    #print gene_name, count
    
    #.iteritems returns 2 tuple, only useful with 2 arguments