a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
op = input("Enter the operator : ")

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(f"{a/b:.5f}")
else :
    print("Invalid Operator ")


