#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

df_ctab = pd.read_csv(sys.argv[1], sep="\t")

df_roi = df_ctab["FPKM"] >= 0
df_high_exp = df_ctab[df_roi]["FPKM"].values

plot.figure()
plt.title("Density of SRR072893 FPKM values")
plt.hexbin(
            
)
