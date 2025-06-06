"""
Factorial
Calculate factorial of a non-negative integer.
"""

def factorial(n):
    if n < 0:
        return None  # Factorial undefined for negative numbers
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    print(factorial(5))   # 120
    print(factorial(0))   # 1
