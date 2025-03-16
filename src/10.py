import random

def get_random_math_problem(difficulty):
    if difficulty == "easy":
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        return f"{num1} + {num2}"
    elif difficulty == "medium":
        num1 = random.randint(11, 100)
        num2 = random.randint(11, 100)
        return f"{num1} - {num2}"
    else:
        num1 = random.randint(101, 1000)
        num2 = random.randint(101, 1000)
        return f"{num1} x {num2}"

difficulty = input("Enter the difficulty level (easy/medium/hard): ")
problem = get_random_math_problem(difficulty)
print(f"What is {problem}")