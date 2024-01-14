import math

# Function to calculate S1
def calculate_S1(a, b, c, x):
    return a * x**2 + b * x + c

# Function to calculate S2
def calculate_S2(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        return a * c * b**2 - 4
    else:
        return 0

# Function to check if a, b, c are sides of a triangle
def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

# Function to calculate perimeter of a triangle
def calculate_perimeter(a, b, c):
    return a + b + c

# Function to calculate area of a triangle using Heron's formula
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Input real numbers a, b, c, and x
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
x = float(input("Enter the value of x: "))

# Calculate and print S1
S1 = calculate_S1(a, b, c, x)
print(f"S1 = {S1}")

# Calculate and print S2
S2 = calculate_S2(a, b, c)
print(f"S2 = {S2}")

# Re-input a, b, c
a = float(input("Re-enter the value of a: "))
b = float(input("Re-enter the value of b: "))
c = float(input("Re-enter the value of c: "))

# Check if a, b, c are sides of a triangle
if is_triangle(a, b, c):
    perimeter = calculate_perimeter(a, b, c)
    area = calculate_area(a, b, c)
    print(f"These are sides of a triangle.")
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")
else:
    print("a, b, c are not sides of a triangle.")
