#!/usr/bin/env python

"""
Plots rolling mean FPKM for two ctab files.

Usage: ./01-rollingMainChrom.py ctab1 ctab2 window size
window size example: 200
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
# import math
# import sklearn import datasets
# import numpy as np

chromosome = ["2L", "2R", "3L", "3R", "4", "X"]

def rolling_mean(file1, file2, window_size):

    df1=pd.read_table(file1)
    df2=pd.read_table(file2)

    for i in chromosome:
        df_roi1 = df1["chr"] == i
        df_roi2 = df2["chr"] == i
    
        df_chrom1 = df1[df_roi1]
        df_chrom2 = df2[df_roi2]

        mean1 = df_chrom1["FPKM"].rolling(window_size).mean()
        mean2 = df_chrom2["FPKM"].rolling(window_size).mean()
        
        
    
        plt.figure()
        plt.plot(mean1, label="Sample1")
        plt.plot(mean2, label="Sample2")
        plt.legend(loc="upper right")
        plt.title("Chromosome {}, FPKM rolling mean (size={})".format(i,window_size) )
        plt.savefig("Chromosome_{}.png".format(i))
        plt.close()
    
    
file1 = open(sys.argv[1])
file2 = open(sys.argv[2])
window_size = int(sys.argv[3])

rolling_mean(file1,file2,window_size)


