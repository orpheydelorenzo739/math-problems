
import random

def generate_random_code():
    """Generates a random Python code snippet"""
    # Initialize a list of operators and keywords
    operators = ["+", "-", "*", "/", "**"]
    keywords = ["if", "else", "while", "for", "in", "range"]
    
    # Generate a random number of lines for the code snippet
    num_lines = random.randint(1, 5)
    
    # Initialize an empty list to store the code lines
    code_lines = []
    
    # Loop through each line and generate a random operation or keyword
    for i in range(num_lines):
        if random.random() < 0.3:
            code_lines.append("{} {} {}".format(
                random.choice(operators),
                random.randint(1, 10),
                random.randint(1, 10)
            ))
        else:
            code_lines.append(random.choice(keywords))
    
    # Return the generated code snippet as a string
    return "\n".join(code_lines)