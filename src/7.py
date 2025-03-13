import random

def solve_math_problem(problem):
    # Randomly solve the math problem
    solution = random.randint(1, 10)
    return solution

if __name__ == "__main__":
    problem = input("Enter a math problem: ")
    solution = solve_math_problem(problem)
    print(f"The solution to the problem {problem} is {solution}.")
