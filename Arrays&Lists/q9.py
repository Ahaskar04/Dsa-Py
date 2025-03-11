#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    for i in range(0, len(nums)):
        if nums[i] in nums[i+1:]: 
            return True
    return False

print(contains_duplicate([1,2,3,4,5, 1]))