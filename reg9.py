import re
text = input("Enter a string: ")
# [^...] means "negation" - matches everything EXCEPT letters, digits, and spaces
cleaned = re.sub(r'[^a-zA-Z0-9 ]', '', text)
print("Cleaned string:", cleaned)
