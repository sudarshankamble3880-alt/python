import re
paragraph = input("Enter text: ")
# Indian PIN codes are exactly 6 digits and do not start with 0
pin_codes = re.findall(r'\b[1-9]\d{5}\b', paragraph)
print("Extracted PIN codes:", pin_codes)
