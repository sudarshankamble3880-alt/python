l1 = [10, 20, 35, 40, 11, 12]

largest = l1[0]
second = l1[0]

for n in l1:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest:", second)
