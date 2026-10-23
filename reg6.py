import re
text = input("Enter text with extra spaces: ")
# \s+ matches 1 or more spaces; replaces them with a single space " "
cleaned_text = re.sub(r'\s+', ' ', text)
print("Cleaned text:", cleaned_text)
