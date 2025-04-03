def cube_root(n):
    """ Calculate the cube root of the given number n """
    if n < 0:
        return None, "Invalid input: Cannot compute the cube root of a negative number."
    else:
        return n ** (1. / 3), "Cube root calculated successfully."

# Example usage
result = cube_root(27)
print(result) # Output: (3.0, 'Cube root calculated successfully.')
