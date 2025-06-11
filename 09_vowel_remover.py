"""
09_vowel_remover.py

Problem:
Remove all vowels from a string.

Steps:
1. Define a set of vowels.
2. Loop through characters and skip vowels.
3. Join and print result.
"""

text = "Beautiful Day"
vowels = "aeiouAEIOU"
no_vowels = ''.join([ch for ch in text if ch not in vowels])

print("Original:", text)
print("Without vowels:", no_vowels)