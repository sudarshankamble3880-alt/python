# 31. Take a list of words and create a dictionary
# where key is word length and value is a list of words having that length.

words = ["cat", "dog", "apple", "book", "pen", "orange"]

d = {}

for word in words:
    length = len(word)

    if length not in d:
        d[length] = []

    d[length].append(word)

print(d)
