"""
Fibonacci Sequence
Print first n Fibonacci numbers starting from 0,1.
"""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # Newline at end

# Example usage
if __name__ == "__main__":
    fibonacci(10)
