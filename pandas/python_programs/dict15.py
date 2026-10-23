# 15. Accept a sentence and create a dictionary containing
# each word and the number of times it occurs.

sentence = input("Enter a sentence: ")

words = sentence.split()
d = {}

for word in words:
    d[word] = d.get(word, 0) + 1

print(d)
