#!/usr/bin/env python

import sys
import pandas as pd

"""
Workflow: read in 
"""

base = sys.argv[1]

df = pd.read_csv(base + "fastq/samples.csv")

d = {}

# each row of dictionary returned as tuple
for _, sample, sex, stage in df.itertuples():
    # make column name meaningful
    # assign right to left: pd data called, sliced, assigned to cell in dictionary, assigned to var
    # instead of indexing with num, will index with transcript name
    col_df = d[sex + "_" + stage] = pd.read_table(
    base + "/results/stringtie/" + sample + "/t_data.ctab", 
    index_col="t_name")["FPKM"]
    
# data frame made from dictionary
df = pd.DataFrame(d)

# write to stdout
df.to_csv(sys.stdout)