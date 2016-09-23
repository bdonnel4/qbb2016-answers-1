#!/usr/bin/env python

import sys

read_1 = open(sys.argv[1])
read_2 = open(sys.argv[1])

count1=0
count2=0

for line in read_1:
    if line == "@"