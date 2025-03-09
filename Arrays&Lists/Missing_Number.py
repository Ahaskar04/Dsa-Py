import numpy as np

def missing_number(arr, n):
    arr_set = set(arr.astype(int))  # Convert NumPy array to set of integers
    print("Missing numbers:")
    for i in range(0, n):  # Use n instead of 'number'
        if i not in arr_set:  # Check against the set
            print(i)

# Create an empty NumPy array
my_array = np.array([], dtype=int)

while True:
    a = input("Enter the contents of array (or 'x' to exit): ")
    if a.lower() == 'x':
        break
    else:
        try:
            b = int(a)
            my_array = np.append(my_array, b)  # Append correctly
        except ValueError:
            print("Invalid input! Please enter an integer or 'x' to exit.")

number = int(input("Enter the number of elements: "))  # Number should be passed as an argument
missing_number(my_array, number)  # Correct function call
