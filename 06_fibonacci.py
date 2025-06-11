"""
06_fibonacci.py

Problem:
Print first n Fibonacci numbers.

Steps:
1. Initialize first two values.
2. Loop and generate next terms.
3. Print all terms.
"""

n = 10
a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()