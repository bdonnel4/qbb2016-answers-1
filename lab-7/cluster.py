#! /usr/bin/env python

from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np
import sys

f = open(sys.argv[1])
gene = []
cfu = []
poly = []
unk = []
int_cell = []
mys = []
mid = []

for line in f:
    if line.startswith("gene"): continue
    fields = line.rstrip("\r\n").split('\t')
    gene.append(fields[0])
    cfu.append(fields[1])
    poly.append(fields[2])
    unk.append(fields[3])
    int_cell.append(fields[4])
    mys.append(fields[5])
    mid.append(fields[6])
    
array = np.array(
                 [cfu,
                  poly, 
                  unk, 
                  int_cell, 
                  mys, 
                  mid,]
                  )
Z1 = linkage(array)
Z2 = linkage(array.T)

indexes = leaves_list(Z1)

ordered_cell_names = []
for i in indexes:
    ordered_cell_names.append(cell_names[i])

array = array[indexes, :]
array = array[:, indexes2]
