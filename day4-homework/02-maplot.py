#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1_ctab=pd.read_csv(sys.argv[1], sep="\t")
df2_ctab=pd.read_csv(sys.argv[2], sep="\t")

df1_roi = df1_ctab["FPKM"] >= 0
df2_roi = df2_ctab["FPKM"] >= 0

df1_exp = np.log(df1_ctab[df1_roi]["FPKM"].values)
df2_exp = np.log(df2_ctab[df2_roi]["FPKM"].values)


count1 = 0
count2 = 0

for row in df1_exp:
    count1 += 1
for row in df2_exp:
    count2 += 2

count_total = count1 + count2
count_tot_float = float(count_total)


avg = (df1_exp+df2_exp)/count_total
diff = df2_exp - df1_exp

val_avg = np.log(df1_exp)
val_diff = np.log(diff)

# val_log1 = np.log(df1_exp)
# val_log2 = np.log(df2_exp)

plt.figure()
plt.scatter(val_log1,val_log2, alpha=0.3)
plt.scatter(avg,diff)
plt.savefig("ma_plot.png")
plt.show()
plt.close()