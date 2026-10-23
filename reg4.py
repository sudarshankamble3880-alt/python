# 4 	Write a program to extract all uppercase letters from a given string

import re
text = input("Enter a string: ")
uppercase = re.findall(r'[A-Z]', text)
print("Uppercase letters:", uppercase)
