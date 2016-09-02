#!/usr/bin/env python


"""
pattern associated with each PC, similarly found in yeast microarray 1998 paper
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

# transpose rows and columns
# df = df.T

# create new PCA (object)
pca = PCA()
fit = pca.fit(df)

x = pca.transform(df)

plt.figure()
plt.plot(fit.components_.T [:,:2])
plt.xticks(range(len(df.columns)), df.columns, rotation=90)
plt.legend()
plt.show()

