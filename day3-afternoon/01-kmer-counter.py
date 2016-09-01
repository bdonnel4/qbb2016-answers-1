#!/usr/bin/env python

"""
Read sequences from a fasta file, count the number of times each 
k-mer occurs across all sequences and print kmers and counts.

Usage: 01-kmer-counter.py k < fasta_file
k = kmer size, on command line
"""

import sys
import fasta

## from fasta import FASTAReader

# command line arguments
k = int(sys.argv[1])

kmer_counts = {}

for identifier, sequence in fasta.FASTAReader(sys.stdin):
    sequence = sequence.upper()
    for i in range(0,len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in kmer_counts:
            kmer_counts[kmer]=0
        kmer_counts[kmer]+=1
        
# for kmer, count in kmer_counts.iteritems():
#     print kmer, count

for kmer in sorted(kmer_counts, key=kmer_counts.get, reverse=True):
    print kmer, kmer_counts[kmer]