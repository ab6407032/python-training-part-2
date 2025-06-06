"""
Multiplication Table
Print multiplication table of a given number up to 10.
"""

def multiplication_table(n):
    for i in range(1, 11):  # Numbers 1 to 10
        print(f"{n} x {i} = {n * i}")

# Example usage
if __name__ == "__main__":
    multiplication_table(5)
