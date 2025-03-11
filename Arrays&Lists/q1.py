#FInd the pairs whose sum equals the number given

def pairs_sum(arr, n):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] == arr[j]):
                continue
            elif arr[i] + arr[j] == n:
                print(arr[i], arr[j])

pairs_sum([1, 2, 3, 4, 5, 6], 6)