#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], index_col=0)

# transpose an array (swap rows and columns = values.T)
corr = np.corrcoef(df.values.T)
corr = pd.DataFrame(corr,columns=df.columns)

print corr

plt.figure()
# rids array of colored boxes
plt.pcolor(corr)
plt.colorbar()
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()