# Write a function to find all pairs of an integer array whose sum is equal to a given number.
def pair_sum(myList, sum):
    for i in range(0, len(myList)):
        for j in range(i+1, len(myList)):
            if (myList[i] + myList[j] == sum):
                print(i)
                print(j)
                
pair_sum([1,2,3,4,5], 4) # 0, 2