#Given 2D list calculate the sum of diagonal elements.

import numpy as nm

def sum(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i][i]
    return sum

print(sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # 15