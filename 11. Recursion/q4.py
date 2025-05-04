# Write a recursive function to convert a decimal number to binary.

def binary(n):
    if n == 0:
        return ''
    else:
        return binary(n // 2) + str(n % 2)

print(binary(5))  # Output: '101'
