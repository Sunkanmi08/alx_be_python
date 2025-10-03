def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return int(num1) + int(num2)
        case "subtract":
            return int(num1) - int(num2)
        case "multiply":
            return int(num1) * int(num2)
        case "divide":
            return int(num1) / int(num2)
