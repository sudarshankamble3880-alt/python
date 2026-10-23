# 2.	Accept a sentence and display all words beginning with the letter A or a.

import re

# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# \b matches word boundaries. [Aa] matches capital A or lowercase a. \w* matches the rest of the word.
words = re.findall(r"\b[Aa]\w*", sentence)

# Print the result
print("Words starting with A or a:", words)
