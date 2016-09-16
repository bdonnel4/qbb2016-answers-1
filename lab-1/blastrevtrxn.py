#!/usr/bin/env python

"""
Usage: ./blastrevtrxn.py blastformat.fa blastp.fa > output.fa


"""

from itertools import izip
import fasta
import sys

nuc_file = fasta.FASTAReader(open(sys.argv[1]))
prot_file = fasta.FASTAReader(open(sys.argv[2]))

nt = []
aa = []

for nuc in nuc_file:
    nt.append(nuc)
    
for prot in prot_file:
    aa.append(prot)
    
# for i in izip(aa,nt):
#     nuc_seq = i[0][1]
#     prot_seq = i[1][1]
#     count = 0
#     new_nuc = []
#     for aminoAcid in prot_seq:
#         if aminoAcid == "-":
#             new_nuc.append("---")
#         else:
#             codon = nuc_seq[count:count+3]
#             count += 3
#             new_nuc.append(codon)
#     print ">" + str(i[0][0])
#     print "".join(new_nuc)
    
for i in izip(aa,nt):
    new_nuc = []
    count = 0
    prot_seq = i[0][1]
    nuc_seq = i[1][1]
    for aminoAcid in prot_seq:
        if aminoAcid == "-":
            new_nuc.append("---")
        else:
            codon = nuc_seq[count:count+3]
            count += 3
            new_nuc.append(codon)
    print ">" + str(i[0][0])
    print "".join(new_nuc)

            
            
    