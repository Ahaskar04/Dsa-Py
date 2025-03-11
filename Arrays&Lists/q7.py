# Write a function to remove the duplicate numbers on given integer array/list.

def remove_duplicates(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)-1):
            if arr[i] == arr[j]:
                arr.pop(j)
    print(arr)
    return arr
    
remove_duplicates([1,2,1,3,4, 4, 5])