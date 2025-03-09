import random

def get_random_python_code():
    # Generate a random integer between 1 and 10
    x = random.randint(1, 10)
    # Generate a random operator (+, -, *, /, %)
    op = random.choice(["+", "-", "*", "/", "%"])
    # Generate a random integer between 1 and 10
    y = random.randint(1, 10)
    # Evaluate the expression using eval()
    result = eval(f"{x}{op}{y}")
    # Return the result as a string
    return f"{x} {op} {y} = {result}"