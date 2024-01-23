# decimal sang octal
def decimal_to_octal(decimal_number):
    # Using the oct() function to convert decimal to octal
    octal_representation = oct(decimal_number)
    return octal_representation

# Accept three real numbers from the user
try:
    a = float(input("Enter the first real number (a): "))
    b = float(input("Enter the second real number (b): "))
    c = float(input("Enter the third real number (c): "))

    # Convert each number to octal and print the result using print() formatting
    print("Octal representation of a: {:o}".format(int(a)))
    print("Octal representation of b: {:o}".format(int(b)))
    print("Octal representation of c: {:o}".format(int(c)))

except ValueError:
    print("Invalid input. Please enter valid real numbers.")
