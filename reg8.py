import re
sentence = input("Enter a sentence: ")
# \w* matches characters before the final 's' or 'S' at a word boundary
words_s = re.findall(r'\b\w*[sS]\b', sentence)
print("Words ending with s:", words_s)
