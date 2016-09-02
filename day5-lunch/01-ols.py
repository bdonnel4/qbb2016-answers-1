#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df_ctab = pd.read_csv(sys.argv[1], sep = "\t")

df_exp = df_ctab["FPKM"].values

df_roi_for = df_ctab["strand"] == "+"
df_for = df_ctab[df_roi_for]

df_roi_rev = df_ctab["strand"] == "-"
df_rev = df_ctab[df_roi_rev]
good_chr = ["2L","2R","3L","3R","4"]

fpkm_list = []

# plus strand parsing
for thing in df_for.itertuples():
    chr_name = thing[2]
    if chr_name not in good_chr:
        continue
    fpkm = thing[-1]
    t_name = thing[6]
    
    fpkm_list.append(fpkm)

# minus strand parsing
for thing in df_rev.itertuples():
    chr_name = thing[2]
    if chr_name not in good_chr:
        continue
    fpkm = thing[-1]
    t_name = thing[6]
    
    fpkm_list.append(fpkm)
    
    
# df_fpkm_list = pd.DataFrame[fpkm_list]

df_chipseq = pd.read_table(sys.argv[2], header=None)
df_mean = df_chipseq[5].values

regression = sm.OLS(fpkm_list,df_mean).fit()
print regression.summary()