# Try... Except

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    print("Addition is: ", result)
except ValueError:
    print("Please enter valid numbers only.")
finally:
    print("Program execution completed.")