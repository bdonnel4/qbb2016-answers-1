#!/usr/bin/env python

"""
Usage: histAlleleFreq.py allelefreq.frqx 
"""

import sys
import matplotlib.pyplot as plt

alleleFreq = open(sys.argv[1])

minorAllele = []

for line in alleleFreq:
    if line.startswith("CHR"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    minor = float(fields[4])
    major = float(fields[6])
    denominator = minor + major
    alFreq = minor/denominator
    minorAllele.append(alFreq)

    
plt.figure()
plt.hist(minorAllele)
# plt.show()
plt.title("Minor allele frequencies")
plt.savefig("histAlleleFreq.png")
plt.close()
