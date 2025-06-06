"""
Vowel Remover
Remove all vowels from a string.
"""

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)

# Example usage
if __name__ == "__main__":
    print(remove_vowels("Hello World"))   # Hll Wrld
    print(remove_vowels("Python"))        # Pythn
