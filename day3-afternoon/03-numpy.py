#!/usr/bin/env python

import sys
# alias of numpy as np
import numpy as np
from statsmodels.stats.weightstats import ttest_ind as ttest


def load_fpkm_from_ctab(my_ctab_filename):
    fpkm_values = []
    for i, line in enumerate(open(my_ctab_filename)):
        if i == 0:
            continue
        fields = line.rstrip("\r\n").split("\t")
        fpkm = float(fields[11])
        fpkm_values.append(fpkm)
    return np.array(fpkm_values)
    
a = load_fpkm_from_ctab(sys.argv[1])
b = load_fpkm_from_ctab(sys.argv[2])
 
print "Correlation {}".format(np.corrcoef(a,b)[0,1])

# compare distribution of both files
# t = ttest(a,b)
# print "t-test t-statistic: {}, p-value: {}, dof: {}".format( t[0],t[1],t[2])
    
print "t-test t-statistic: {}, p-value: {}, dof: {}".format(*ttest(a,b))

# a = np.array(fpkm_values)

# print a
# print a.shape
# print a.dtype
# print np.mean(a)
# print np.std(a)
# print np.max(a)
# print np.min(a)