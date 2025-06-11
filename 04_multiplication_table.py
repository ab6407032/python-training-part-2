"""
04_multiplication_table.py

Problem:
Print the multiplication table for a given number.

Steps:
1. Loop from 1 to 10.
2. Multiply the number with loop variable.
3. Print formatted result.
"""

num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")