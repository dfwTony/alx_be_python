# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: add, subtract, multiply, or divide.
    Handles division by zero and invalid operations.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
    
num1 = int(input("Enter your number 1: "))
num2 = int(input("Enter your number 2: "))

operations = perform_operation(num1, num2, input("Choose an operation (add/subtract/multiply/divide): ").lower())

print(operations)