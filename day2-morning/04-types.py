#!/usr/bin/env python

print "Basic types"

a_string = "this is a string"

integer = 7

flo = 5.6

truth = True
false = False


for value in (a_string, integer, flo, truth):
    print value, type(value)

print "\nList and tuples"

a_list = [1,2,4,5,6]

a_tuple = (1,2,3,4,5,6)

print a_list, type (a_list)
print a_tuple, type (a_tuple)

a_list[3] = 777
print a_list

# throws exception (tuples cannot be modified)
# a_tuple[3] = 777
# print a_tuple

print "\nRefs and Lists"

my_var_a = [1,2,3,4]

my_var_b = my_var_a

my_var_c = list(my_var_a)

my_var_a[2] = 99999

print my_var_b

print my_var_c

