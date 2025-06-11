"""
07_prime_number.py

Problem:
Check if a number is prime.

Steps:
1. Prime has only two divisors.
2. Check from 2 to sqrt(n).
3. Print result.
"""

num = 29
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print(f"{num} is prime:" if is_prime else f"{num} is not prime.")