#!/usr/bin/env python

"""
Usage: ./spadesparser.py contigs.fasta

Purpose: compute the number of contigs,
minimum/maximum/average contig length, and N50
"""

import sys
import fasta

spades_file = fasta.FASTAReader(open(sys.argv[1]))

contigs = []
count = 0
sequence_length = []
length = 0

for identifier, sequence in spades_file:
    count += 1
    l = len(sequence)
    sequence_length.append(l)
    length += l


g2 = length/2.0
cum_length = 0

for l in sequence_length:
    cum_length += l
    if cum_length >= g2:
        n50 = len(sequence)
        break
        

maxContig = max(sequence_length)
minContig = min(sequence_length)

print "Number of contigs: ", count
print "Max of contigs: ", maxContig
print "Min of contigs: ", minContig
print "N50: ", n50
