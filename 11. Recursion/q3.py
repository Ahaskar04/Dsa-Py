# Problem: Write a recursive function to find the greatest common divisor (GCD) of two numbers.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(48, 18))