def Factorial(n):
    fact = 1
    if n<0:
        print("Invalid input")
    elif n==0:
        fact = 1
    elif n>0:
        for i in range (1,n+1):
            fact*=i
        return fact

n = int(input("Enter a number "))
print(f"Factorial of {n} = {Factorial(n)}")
