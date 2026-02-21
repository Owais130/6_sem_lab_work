import math

n = int(input("Enter a number : "))

def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x

if is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4):
    print("Fibonacci")
else:
    print("Not Fibonacci")
