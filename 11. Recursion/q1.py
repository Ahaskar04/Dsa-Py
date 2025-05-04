# Find sum of digits of a number using recursion

import math
def sumDigits(number):
    if number == 0: return 0
    else:
        return number % 10 + sumDigits(math.floor(number/10))
        
print(sumDigits(12345))