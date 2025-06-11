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

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i

print(f"Factorial of {n} is {fact}")