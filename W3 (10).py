def Add(a,b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
print("Sum = ",Add(a,b))
