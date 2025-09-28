# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations using a dictionary mapping.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the arithmetic operation, or an error message.
    """

    # Define the operations as a dictionary of lambdas (anonymous functions)
    operations = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: a / b if b != 0 else "Error: Division by zero"
    }

    # Get the operation function from the dictionary
    func = operations.get(operation)

    # If operation exists, call it; otherwise return an error
    if func:
        return func(num1, num2)
    else:
        return "Error: Invalid operation"

