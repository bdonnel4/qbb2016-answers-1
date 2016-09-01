#!/usr/bin/env python

def returns_none():
    pass
    
v = returns_none()

print "v", v

print "false?", v == False
print "true?", v == True
print "0", v == 0
print None, v is None