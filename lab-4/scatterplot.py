#!/usr/bin/env python

"""
Usage: scatterplot.py genotypePCA.eigenvec
"""

import sys
import matplotlib.pyplot as plt

genoEigenvac = open(sys.argv[1])
x=[]
y=[]

for line in genoEigenvac:
    fields = line.rstrip("\r\n").split(" ")
    x.append(fields[2])
    y.append(fields[3])

plt.figure()
plt.scatter(x,y)
plt.title("PCA of genotype data")
plt.savefig("scatterplotPCAgeno.png")
plt.close()