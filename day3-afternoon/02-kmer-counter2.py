#!/usr/bin/env python

"""
Read sequences from a fasta file, for each sequence count the number of times each 
k-mer occurs across all sequences and print 10 most frequent kmers and counts.

Usage: 01-kmer-counter.py k < fasta_file
k = kmer size, on command line
"""

import sys
import fasta

## from fasta import FASTAReader

# command line arguments
k = int(sys.argv[1])

for identifier, sequence in fasta.FASTAReader(sys.stdin):
    sequence = sequence.upper()
    kmer_counts = {}
    for i in range(0,len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in kmer_counts:
            kmer_counts[kmer]=0
        kmer_counts[kmer]+=1
    print "----", identifier, "----"
    # for kmer, count in kmer_counts.iteritems():
    #     print kmer, count

    for i, kmer in enumerate(sorted(kmer_counts, 
                                key=kmer_counts.get, 
                                reverse=True)):
        if i >= 10:
            break
        print kmer, kmer_counts[kmer]
        
