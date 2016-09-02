#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table(sys.argv[1])

df_roi_for = df["strand"] == "+"
df_for = df[df_roi_for]

df_roi_rev = df["strand"] == "-"
df_rev = df[df_roi_rev]

df_start = []
d = {}
good_chr = ["2L","2R","3L","3R","4"]

# df_start.append(df_for["start"])
# df_start.append(df_rev["end"])


# plus strand parsing
for thing in df_for.itertuples():
    chr_name = thing[2]
    if chr_name not in good_chr:
        continue
    start = thing[4] -500
    end = thing[4] +500
    t_name = thing[6]
    
    print chr_name,"\t",start,"\t",end,"\t",t_name

# minus strand parsing
for thing in df_rev.itertuples():
    chr_name = thing[2]
    if chr_name not in good_chr:
        continue
    start = thing[4] -500
    end = thing[4] +500
    t_name = thing[6]
    
    print chr_name,"\t",start,"\t",end,"\t",t_name


    



