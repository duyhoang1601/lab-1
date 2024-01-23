# Accept three real numbers from the user
try:
    a = float(input("Enter the first real number (a): "))
    b = float(input("Enter the second real number (b): "))
    c = float(input("Enter the third real number (c): "))

    # Display each number with 2 decimal places using print() formatting
    print("Float representation of a: {:.2f}".format(a))
    print("Float representation of b: {:.2f}".format(b))
    print("Float representation of c: {:.2f}".format(c))

except ValueError:
    print("Invalid input. Please enter valid real numbers.")
