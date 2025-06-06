"""
FizzBuzz
Print numbers 1 to n; multiples of 3 print "Fizz", multiples of 5 print "Buzz", multiples of both print "FizzBuzz".
"""

def fizzbuzz(n):
    for i in range(1, n + 1):  # Loop from 1 to n inclusive
        if i % 3 == 0 and i % 5 == 0:  # Divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Divisible by 3 only
            print("Fizz")
        elif i % 5 == 0:  # Divisible by 5 only
            print("Buzz")
        else:
            print(i)  # Print the number itself if none above

# Example usage
if __name__ == "__main__":
    fizzbuzz(15)
