"""
03_sum_of_digits.py

Problem:
Find the sum of digits of a number.

Steps:
1. Convert number to string or use % and //.
2. Sum digits using loop or list comprehension.
3. Print result.
"""

number = 12345
total = sum(int(digit) for digit in str(number))

print(f"Sum of digits of {number} is {total}")