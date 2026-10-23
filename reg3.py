#3.	Write a program to count the occurrences of vowels in a given string using regular expressions.

import re

# Ask the user for input
text = input("Enter a string: ")

# Find all vowels (both lowercase and uppercase)
vowels = re.findall(r'[aeiouAEIOU]', text)

# len() counts the total number of elements in the list
vowel_count = len(vowels)

print("Total number of vowels:", vowel_count)
print("The vowels found are:", vowels)
