import re
paragraph = input("Enter text containing dates: ")
# Matches 2 digits for day, 2 for month, 4 for year separated by hyphens
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', paragraph)
print("Extracted dates:", dates)
