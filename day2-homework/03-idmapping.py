#!/usr/bin/env python

import sys

mapdict = {}

def identifier_mapping(mapout, ctab, default):
    for line in mapout:
        fields = line.rstrip("\r\n").split()
        swiss_AC = fields[-2]
        fly_AC = fields[-1]
        mapdict[fly_AC] = swiss_AC
    for i, line in enumerate(ctab):
        if i==0:
            continue
        fields2 = line.rstrip("\r\n").split("\t")
        gene_name = fields2[9]
        if gene_name in mapdict:
            fields2[9] = mapdict[gene_name]
            print "\t".join(fields)
            
identifier_mapping(open(sys.argv[1]), open(sys.argv[2], sys.argv[3])