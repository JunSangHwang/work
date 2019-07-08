#1
import sys

def max_select( *data_list ):
    maximum = sys.float_info.min

    for value in data_list:
        if value > maximum:
            maximum = value

    return maximum


print(max_select(3,4,5,6,7))


#2
def min_select( *data_list ):
    minimum = sys.float_info.max

    for value in data_list:
        if value < minimum:
            minimum = value

    return minimum


print(min_select(3,4,5,6,7))





#  3.
def my_sum(*a):
    add=0
    for i in a:
        add= add+i
    return add

print(my_sum(4,6,5))
    

# 4.
def my_avg(*b):
    add=0
    for i in b:
        add=add+i
    avg = add / len(b)
    return avg

print(my_avg(4,5,6))
