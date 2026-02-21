def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter 1st number \n"))
y = int(input("Enter 2nd number \n"))
print("GCD of",x,"and",y,"is",gcd(x,y))
