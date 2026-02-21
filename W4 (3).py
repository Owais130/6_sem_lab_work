def Effective_Area():
    R = int(input("Enter Outer Radius : "))
    r = int(input("Enter inner Radius : "))
    EA = 0
    if R<=r:
        print("Invalid input : Outer Radius is Smaller")
    else:
        EA = (22/7)*(R**2-r**2)
        return EA

print(f"Effective Area = {Effective_Area()}")

    
        
