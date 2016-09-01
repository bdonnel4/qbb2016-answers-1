#!/usr/bin/env python

"""

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import math
# import sklearn import datasets
# import numpy as np

df1=pd.read_table(sys.argv[1])
df2=pd.read_table(sys.argv[2])

df_roi1=df1["gene_name"] == "Sxl"
df_roi2=df2["gene_name"] == "Sxl"

df1_v2 = df1[df_roi1]
df2_v2 = df2[df_roi2]

df_exp1 = df1_v2["FPKM"] > 0
df_exp2 = df2_v2["FPKM"] > 0

df1_v3 = df1_v2[df_exp1]
df2_v3 = df2_v2[df_exp2]

abundance1 = df1_v3["FPKM"]
abundance2 = df2_v3["FPKM"]

print abundance1
print abundance2

samples = ["SRR072893", "SRR072915"]

plt.figure()
plt.title("Abundance measurements for all Sxl isoforms")
plt.boxplot(
            [abundance1, abundance2],
            labels=samples,
            )
plt.xlabel("Samples")
plt.ylabel("log(FPKM)")
plt.yscale("log")
plt.savefig("sxlBoxplot.png")
plt.close()