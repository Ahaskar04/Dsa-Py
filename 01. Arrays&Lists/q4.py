#Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
def middle(arr):
    return arr[1:-1]

print(middle([1, 2, 3, 4, 5, 6])) # [2, 3, 4, 5]