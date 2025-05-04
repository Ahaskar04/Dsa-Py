# Given an array of numbers, write a function that returns the product of all the numbers in the array.

def productOfArray(arr):
    if len(arr) == 0: return 1 
    else: return arr.pop() * productOfArray(arr)