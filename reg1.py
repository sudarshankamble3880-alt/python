#1.Write a Python program using regular expressions to extract all digits from a given string

import re

# Ask the user for input
text = input("Enter a string: ")

# Find all individual digits
digits = re.findall(r'\d', text)

# Print the result
print("Extracted digits:", digits)

