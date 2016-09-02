#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_ctab = pd.read_csv(sys.argv[1], sep="\t")

df_roi = df_ctab["FPKM"] > 0
df_high_exp = df_ctab[df_roi]["FPKM"].values

val_log = np.log(df_high_exp)
print val_log



plt.figure()                  # Open blank canvas
plt.hist(val_log)                   # Generate a histogram of the data, with defaul settings
plt.savefig("first_hist.png") # Save the figure
plt.title("Histogram of FPKM values for SRR072893") # Add a title to the top
plt.ylabel("y axis")            # Label the y-axis
plt.xlabel("x axis")              # Label the x-axis with the name of the feature we used
plt.savefig("893_hist_FPKM.png")      # Save figure as .png
plt.close()                        # Close the canvas
