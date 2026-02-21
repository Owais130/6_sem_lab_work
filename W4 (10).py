def volume_sphere(r):
    volume = (4/3)*(22/7)* r**3
    return volume

R = int(input("Enter Radius : "))

print(f"Volume of Sphere with Radius {R} is {volume_sphere(R):.2f}",)
