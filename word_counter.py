"""
Word Counter
Count the number of words in a string.
"""

def word_count(text):
    words = text.strip().split()
    return len(words)

# Example usage
if __name__ == "__main__":
    print(word_count("Hello world! This is Python."))  # 5
    print(word_count("    "))                           # 0
