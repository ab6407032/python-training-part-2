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

text = "Madam"
normalized = text.replace(" ", "").lower()
is_palindrome = normalized == normalized[::-1]

print(f"'{text}' is a palindrome:" if is_palindrome else f"'{text}' is not a palindrome.")