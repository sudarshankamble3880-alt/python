import re
sentence = input("Enter a sentence: ")
# \b marks word boundaries, \w{5} matches exactly 5 letters/digits
words_5 = re.findall(r'\b\w{5}\b', sentence)
print("5-character words:", words_5)
