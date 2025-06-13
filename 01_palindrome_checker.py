"""
01_palindrome_checker.py

Problem:
Check if a string is a palindrome.

Steps:
1. Take a string as input.
2. Normalize it (lowercase, remove spaces).
3. Compare the string to its reverse.
4. Print result.
"""

def is_palindrome(text):
    normalized = text.replace(" ", "").lower()    # Remove spaces and convert to lowercase
    return normalized == normalized[::-1]         # Compare with reversed string

# Example usage
input_text = "Madam"
if is_palindrome(input_text):
    print(f"'{input_text}' is a palindrome.")
else:
    print(f"'{input_text}' is not a palindrome.")
