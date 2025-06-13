"""
08_word_counter.py

Problem:
Count number of words in a sentence.

Steps:
1. Split the sentence on spaces.
2. Use len() to count words.
"""

def count_words(sentence):
    word_count = len(sentence.split())  # Split by spaces and count parts
    return word_count

# Example usage
sentence = "This is a sample sentence"
print("Number of words:", count_words(sentence))
