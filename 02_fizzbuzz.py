"""
02_fizzbuzz.py

Problem:
Print numbers 1 to 100. For multiples of 3 print 'Fizz', of 5 print 'Buzz',
and for both print 'FizzBuzz'.

Steps:
1. Loop from 1 to 100.
2. Use if-elif to check divisibility.
3. Print accordingly.
"""

def fizzbuzz(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage
fizzbuzz(1, 100)
