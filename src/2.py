def get_random_math_problem(max_value):
    # Generate two random numbers between 1 and max_value
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    
    # Get a random operation (+, -, *, /)
    op = random.choice(['+', '-', '*', '/'])
    
    # Return the problem and the correct answer
    return f"{num1} {op} {num2} = ?", num1 {op}(num2)
