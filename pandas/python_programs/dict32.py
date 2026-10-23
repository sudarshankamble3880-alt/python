# 32. Take a list of integers and a target value.
# Find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15]
target = 9

d = {}

for i in numbers:
    x = target - i

    if x in d:
        print("Numbers are:", x, i)
        break

    d[i] = 1
