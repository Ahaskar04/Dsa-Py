# Find the maximum product of two integers in an array where all elements are positive.
import numpy as nm

def max_product(arr):
    sum = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > sum:
                sum = product
    return sum

print(max_product([1, 2, 3, 4, 5, 6]))