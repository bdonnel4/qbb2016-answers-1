#!/usr/bin/env python


"""
, similarly found in yeast microarray 1998 paper
"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# machine learning package
from sklearn.decomposition import PCA

df = pd.read_csv(sys.argv[1], index_col=0)

# .shape = tuple of sets given
n, p = df.shape

df = df.T

pca = PCA()

fit = pca.fit(df)
x = fit.transform(df)

colors = []
for name in df.T.columns:
    if "female" in name:
        colors.append("purple")
    else:
        colors.append("orange")

plt.figure()
# graph principal component 1 and 2
# plt.scatter(x[:,0],x[:,1], c=colors, edgecolor="None")
colnames = df.T.columns

# for i in range(len(colnames)):
#     plt.annotate(colnames[i], (x[i,0], x[i,1]))

n_pcs = 8

x2 = x[:,:n_pcs]

for i in range(n_pcs):
    for j in range(n_pcs):
        plt.subplot(n_pcs,n_pcs,i+j*n_pcs+1)
        plt.scatter(x2[:,i], x2[:,j])


plt.show()