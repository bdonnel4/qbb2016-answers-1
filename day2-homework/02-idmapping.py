#!/usr/bin/env python

import sys

mapping = {}

def id_mapping(mapfile, c_tab, mode):
    for line in mapfile:
        fields = line.rstrip( "\r\n").split()
        swiss_AC = fields[0]
        fly_AC = fields[-1].strip()
        mapping[fly_AC] = swiss_AC
    for i, line in enumerate(c_tab):
        if i==0:
            continue
        fields2 = line.rstrip( "\r\n").split("\t")
        gene_name = fields2[8].strip()
        if gene_name in mapping:
            fields2[8] = mapping[gene_name]
            print "\t".join(fields2)
        elif mode =="d":
            fields2[8] = "."
            print "\t".join(fields2)
        else:
            continue
            
id_mapping(open(sys.argv[1]), open(sys.argv[2]), sys.argv[3])
        
    
