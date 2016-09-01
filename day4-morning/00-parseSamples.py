#!/usr/bin/env python

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
#return sample/sex/stage column contents only
# print df["sample"]
# print df[0:5]
# print df["sample"][0:5]

df_roi = df["sex"] == "female"
print df_roi


# file = open(sys.argv[1])
#
# for i, line in enumerate(file):
#     if i == 0:
#         continue
#     fields = line.rstrip("\r\n").split(",")
#     print fields[0]
#
# file.close()