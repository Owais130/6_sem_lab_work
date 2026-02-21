def average_of_marks(marks):
    return sum(marks) / 5

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def rectangle_perimeter(length, width):
    return 2 * (length + width)

marks = [30, 25, 20, 30, 40]
avg = average_of_marks(marks)
print("Average =", avg)

temperature = 37
#n=int(input("Enter Temperature in °C"))
fahrenheit = celsius_to_fahrenheit(temperature)
print("Temperature in Fahrenheit =", fahrenheit, "°F")

length = 10
width = 5
perimeter = rectangle_perimeter(length, width)
print("Perimeter of the Rectangle =", perimeter)
