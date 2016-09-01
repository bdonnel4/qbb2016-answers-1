#!/usr/bin/env python

# Option 1

# f = open("temp.fa")

# Option 2
# import sys

# f = sys.stdin

# Option 3
import sys

f = open(sys.argv[1])


# print f
# print type(f)
# print f.read()

# Q - open some number of files

# file_handles=[]
# for filename in sys.argv[1:]:
#     file_handles.append(open(filename))

# reading files line by line

for i, line in enumerate( f.readlines() ):
    #chomp in perl, remove new line, other whitespaces on right side (rstrip) or left side (lstrip)
    line = line.rstrip("\r\n")
    #searching for sequence line, not comments
    if line.startswith(">"): 
        #same as if line[0] == ">"
        continue
    print i, line [10:30]
    #printing line number and seq line
    
    
    