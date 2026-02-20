x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

numerator = 1 + (x / y) + (x ** y)
denominator = 2 + (y / x) + (y ** x)

result = numerator / denominator

print("Result =", result)
