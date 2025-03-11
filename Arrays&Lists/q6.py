# Write a function to remove the duplicate numbers on given integer array/list.
import numpy

def first_second(my_list):
    my_list.sort()
    return my_list[-1], my_list[-2]

print(first_second([1, 2, 3, 4, 5, 6])) # (6, 5)

# My Solution:
def first_second(my_list):
    largest = 0
    second = 0
    for i in range (0, len(my_list)):
        if (my_list[i] > largest):
            largest = my_list[i]
    for i in range (0, len(my_list)):
        if (my_list[i] > second & my_list[i] < largest):
            second = my_list[i]
    # print (largest)
    # print(second)
    return largest, second

list = [1,3,43,5,6]
first_second(list)