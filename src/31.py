def calculate_sum(a: float, b: float) -> float:
    return a + b

def find_median(numbers):
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers)//2] + numbers[(len(numbers)//2)-1]) / 2
    else:
        return numbers[len(numbers)//2]

# Example usage
result = calculate_sum(5, 3)
print("Sum:", result)

median_value = find_median([1, 2, 3, 4])
print("Median:", median_value)
