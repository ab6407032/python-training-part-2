"""
Palindrome Checker
Checks if a given string is a palindrome (ignores spaces and case).
"""

def is_palindrome(s):
    # Remove spaces and convert to lowercase to ignore case and spaces
    s = s.replace(" ", "").lower()
    # Check if string equals its reverse
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    print(is_palindrome("Madam"))          # True
    print(is_palindrome("Hello"))          # False
    print(is_palindrome("A man a plan a canal Panama"))  # True
