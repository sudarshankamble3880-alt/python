import re
sentence = input("Enter a sentence: ")
# \b(\w+)\b captures a word; \s+\1 checks if that exact captured word repeats next
repeats = re.findall(r'\b(\w+)\s+\1\b', sentence, re.IGNORECASE)
print("Repeated words:", repeats)
