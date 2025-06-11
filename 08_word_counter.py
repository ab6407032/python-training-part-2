"""
08_word_counter.py

Problem:
Count number of words in a sentence.

Steps:
1. Split the sentence on spaces.
2. Use len() to count words.
"""

sentence = "This is a sample sentence"
word_count = len(sentence.split())

print("Number of words:", word_count)