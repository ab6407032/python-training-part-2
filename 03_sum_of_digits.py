"""
03_sum_of_digits.py

Problem:
Find the sum of digits of a number.

Steps:
1. Convert number to string or use % and //.
2. Sum digits using loop or list comprehension.
3. Print result.
"""

def sum_of_digits(number):
    total = 0 #3
    for digit in str(number): #123 (1) 1
        total += int(digit) # 1 + 2
    return total
    
r = sum_of_digits(123)
print(r)
    
