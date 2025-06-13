"""
06_fibonacci.py

Problem:
Print first n Fibonacci numbers.

Steps:
1. Initialize first two values.
2. Loop and generate next terms.
3. Print all terms.
"""

def fibseq(n):
    a = 0
    b = 1

    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=' ')
        temp = a       # Save current a
        a = b          # Move b to a
        b = temp + b   # Use saved a to compute new b

    print()
