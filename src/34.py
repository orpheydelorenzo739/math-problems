def multiply_numbers(a: int, b: int) -> int:
    """
    Multiply two integers and return the product.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
        
    Returns:
        int: The product of the two numbers.
    """
    return a * b

def main():
    # Example usage
    num1 = 5
    num2 = 3
    result = multiply_numbers(num1, num2)
    print(f"The product is: {result}")

if __name__ == "__main__":
    main()
