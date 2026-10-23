# 23. Given a list of numbers, create a dictionary
# containing each unique number and its frequency.

numbers = [1, 2, 2, 3, 4, 1, 3, 2, 5]

d = {}

for i in numbers:
    d[i] = d.get(i, 0) + 1

print(d)
