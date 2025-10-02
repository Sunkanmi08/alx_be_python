import sys
num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        print(f"The result is {int(num1) + int(num2)}.")
    case "-":
        print(f"The result is {int(num1) - int(num2)}.")
    case "*":
        print(f"The result is {int(num1) * int(num2)}.")
    case '/':
        if num2 == "0":
            print("Cannot divide by zero.")
            sys.exit()
        print(f"The result is {int(num1) / int(num2)}.")