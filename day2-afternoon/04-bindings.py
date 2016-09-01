#!/usr/bin/env python

def my_func(x):
    return x
    
out = my_func("Hello world")

new_string = "Simon says: '%s' " % out
new_string2 = "Jack says: '{}' {} ".format(out, "Pecans")

print new_string
print new_string2

