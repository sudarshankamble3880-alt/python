# 14. Accept a string from the user and create a dictionary
# containing each character and its frequency.

text = input("Enter a string: ")

d = {}

for i in text:
    d[i] = d.get(i, 0) + 1

print(d)
