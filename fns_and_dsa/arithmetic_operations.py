def perform_operation(num1, num2, operation):
# Ensure operation is case-insensitive
operation = operation.lower().strip()

```
if operation == "add":
    return num1 + num2
elif operation == "subtract":
    return num1 - num2
elif operation == "multiply":
    return num1 * num2
elif operation == "divide":
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2
else:
    return "Error: Invalid operation"
```

Arithmetic Operations
Enter the first number: 8
Enter the second number: 4
Enter the operation (add, subtract, multiply, divide): multiply
Result: 32.0
