a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

a = a ^ b
b = a ^ b
a = a ^ b

print(f"a = {a} and b = {b}")
