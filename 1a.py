def calculate_multiplication_and_sum(num1, num2):

    multiplication_result = num1 * num2
    sum_result = num1 + num2

    print(f"Multiplication Result: {multiplication_result}")
    print(f"Sum Result: {sum_result}")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    calculate_multiplication_and_sum(num1, num2)

except ValueError:
    print("Invalid input. Please enter valid numbers.")
