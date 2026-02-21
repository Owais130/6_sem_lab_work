a = int(input("Enter value of a : "))
fact = 1
if a<0:
    print("Error")
elif a==0:
    print(f"factorial of {a} = 1")
else:
    for i in range(1,a+1):
        fact *= i
print(f"factorial of {a} = {fact}")
