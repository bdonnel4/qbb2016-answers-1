#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# machine learning package
from sklearn.decomposition import PCA

df = pd.read_csv(sys.argv[1], index_col=0)

# .shape = tuple of sets given
n, p = df.shape

#transpose rows and columns
df = df.T

# create new PCA (object)
pca = PCA()
fit = pca.fit(df)

plt.figure()
plt.bar(range(p), fit.explained_variance_ratio_)
plt.show()