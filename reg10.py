import re
sentence = input("Enter a sentence: ")
# \w+ finds sequences of alphanumeric characters (words)
words = re.findall(r'\w+', sentence)
print("Word count:", len(words))
