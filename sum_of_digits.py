"""
Sum of Digits
Calculate the sum of digits of a given integer.
"""

def sum_of_digits(num):
    total = 0
    # Convert number to string to iterate over each digit
    for digit in str(abs(num)):  # abs() handles negative numbers
        total += int(digit)
    return total

# Example usage
if __name__ == "__main__":
    print(sum_of_digits(1234))    # 10
    print(sum_of_digits(-567))    # 18
