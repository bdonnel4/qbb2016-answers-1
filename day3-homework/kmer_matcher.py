#!/usr/bin/env python

"""
Read sequences from a fasta file and query file, for each sequence match 
k-mer that occurs across query file.

Usage: kmer_matcher.py <target.fa> <query.fa> <k>
k = kmer size, on command line
"""

import sys
import fasta

## from fasta import FASTAReader

def kmer_match(target, query, k):
    k = int(k)
    kmer_start = {}
    seq_name = {}

    for identifier, sequence in fasta.FASTAReader(target):
        sequence = sequence.upper()
        for i in range(0,len(sequence) - k):
            kmer = sequence[i:i+k]
            if kmer not in kmer_start:
                kmer_start[kmer]= []
                seq_name[kmer] = []
            kmer_start[kmer].append(i)
            seq_name[kmer].append(identifier)
    
    # for kmer, count in kmer_counts.iteritems():
    #     print kmer, count
    
    query_match = {}
    query_name = {}
    
    for identifier, sequence in fasta.FASTAReader(query):
        sequence = sequence.upper()
        for i in range(0,len(sequence) - k):
            kmer = sequence[i:i+k]
            if kmer in query_match:
                query_match[kmer].append(i)
            if kmer in kmer_start:
                query_match[kmer]=[]
                query_match[kmer].append(i)
                query_name[kmer]=[]
                query_name[kmer].append(seq_name[kmer])
            
    for identifier in query_match:
        print "Identifier: ", identifier
        print "Target_name: ", query_name[identifier]
        print "Target_start: ", kmer_start[identifier]
        print "Query_start: ", query_match[identifier], "\n"
    
kmer_match(open(sys.argv[1]),open(sys.argv[2]),sys.argv[3])

# for i, kmer in enumerate(sorted(kmer_counts,
#                             key=kmer_counts.get,
#                             reverse=True)):
#     if i >= 10:
#         break
#     print kmer, kmer_counts[kmer]
#
