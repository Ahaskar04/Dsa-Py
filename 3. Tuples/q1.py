# Write a function that calculates the sum and product of all elements in a tuple of numbers.
def sum_product(input_tuple):
    sum = 0
    product = 1
    for i in input_tuple:
        sum += i
        product *= i
    return sum, product
    

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)

