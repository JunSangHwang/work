#1
import sys

def max_select( *data_list ):
    maximum = sys.float_info.min

    for value in data_list:
        if value > maximum:
            maximum = value

    return maximum


#2
def min_select( *data_list ):
    minimum = sys.float_info.max

    for value in data_list:
        if value < minimum:
            minimum = value

    return minimum





#  3.
def my_sum(*a):
    add=0
    for i in a:
        add = add+i
    return add
    

# 4.
def my_avg(*b):
    add=0
    for i in b:
        add=add+i
    avg = add / len(b)
    return avg
