"""
07_prime_number.py

Problem:
Check if a number is prime.

Steps:
1. Prime has only two divisors.
2. Check from 2 to sqrt(n).
3. Print result.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
num = 29
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
