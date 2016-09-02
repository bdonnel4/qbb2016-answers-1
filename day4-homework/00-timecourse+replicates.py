#!/usr/bin/env python

"""
Usage: ./01-timecourse.py <metadata.csv> <replicatedata.csv <ctab_dir>
e.g. ./01-timecourse.py samples.csv replicates.csv ~/data/results/stringtie
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_meta = pd.read_csv(sys.argv[1])
df_rep = pd.read_csv(sys.argv[2])
ctab_dir = sys.argv[3]

fem_Sxl = []
fem_rep_Sxl = []

df_roi_fem=df_meta["sex"] == "female"
for sample in df_meta[df_roi_fem]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df_roi2 = df["t_name"] == "FBtr0331261"
    # .values changes format from panda dataframe 
    # to numpy (just values), for matplotlib to read
    
    # store FPKM value into fem_Sxl list
    fem_Sxl.append(df[df_roi2]["FPKM"].values)
    
df_roi_frep=df_rep["sex"] == "female"
for sample in df_rep[df_roi_frep]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df_roi2 = df["t_name"] == "FBtr0331261"
    # .values changes format from panda dataframe 
    # to numpy (just values), for matplotlib to read
    
    # store FPKM value into fem_Sxl list
    fem_rep_Sxl.append(df[df_roi2]["FPKM"].values)

male_Sxl = []
male_rep_Sxl = []

df_roi_male=df_meta["sex"] == "male"
for sample in df_meta[df_roi_male]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df_roi2 = df["t_name"] == "FBtr0331261"
    # .values changes format from panda dataframe 
    # to numpy (just values), for matplotlib to read
    
    # store FPKM value into fem_Sxl list
    male_Sxl.append(df[df_roi2]["FPKM"].values)
    
df_roi_mrep=df_rep["sex"] == "male"
for sample in df_rep[df_roi_mrep]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df_roi2 = df["t_name"] == "FBtr0331261"
    # .values changes format from panda dataframe 
    # to numpy (just values), for matplotlib to read
    
    # store FPKM value into fem_Sxl list
    male_rep_Sxl.append(df[df_roi2]["FPKM"].values)


plt.figure()
x = [1,2,3,4,5,6,7,8]
xlabel=["10","11","12","13","14A","14B","14C","14D"]
plt.xticks(x,xlabel,rotation='horizontal')
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.title("Sxl")
plt.plot(fem_Sxl, 'r-')
plt.plot(male_Sxl, 'b-')
plt.plot([4,5,6,7], male_rep_Sxl, 'b.')
plt.plot([4,5,6,7], fem_rep_Sxl, 'r.')
# plt.show()
plt.savefig("timecourse.png")
plt.close()

