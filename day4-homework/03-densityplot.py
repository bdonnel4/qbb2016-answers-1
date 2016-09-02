#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

df_ctab = pd.read_table(sys.argv[1])

df1_exp = df_ctab["FPKM"].values

density = gaussian_kde(df1_exp)

plt.figure()
plt.title("Density of SRR072893 FPKM values")
xs = np.linspace(np.min(df1_exp),100,100)
plt.plot(xs,density(xs))
plt.savefig("density_plot.png")
plt.close


