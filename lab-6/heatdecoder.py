#!/usr/bin/env python

import h5py
import sys
import numpy as np

peaks = open(sys.argv[1])

file = h5py.File("enrichmentout.heat")

# file.keys()[u'0.counts',u'0.expected',u'0.positions',u'regions']

regions = file['regions'][...]
counts = file['0.counts'][...]
# counts1 = np.ma.masked_equal(counts,0)
positions = file['0.positions'][...]
expected = file['0.expected'][...]
# expected1 = np.ma.masked_equal(counts,0)

nonzero_counts = np.nonzero(counts)
# nonzero_exp = np.nonzero(expected)

enrichments = np.log(counts/expected)
# enrichments = np.ma.filled(enrichments,0)

# print enrichments
dict_pos={}
for i,line in enumerate(peaks):
    if line.startswith("#Chromosome"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    chrom = fields[0]
    # print(chrom)
    if chrom == "chrX":
        dict_pos[fields[1]]= fields[1]

for i, line1 in enumerate(positions):
    for element in dict_pos:
        if int(element) >= line1[0] and int(element) <= line1[1]:
            k=0;
            for anum,line2 in enumerate(enrichments[i]):
                k=k+1;
                if k == 1:
                    maximum = anum
                elif anum > maximum:
                    maximum = anum
                    position = line2
            print "enumerate: ", i
            print "line: ", position
                
                
    




