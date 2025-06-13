"""
05_factorial.py

Problem:
Calculate factorial using loop.

Steps:
1. Set result = 1.
2. Loop from 1 to n.
3. Multiply result each time.
4. Print result.
"""

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Example usage
n = 5
result = factorial(n)
print(f"Factorial of {n} is {result}")
