import math

num = int(input("Enter a number: "))
root = int(math.sqrt(num))

c = 0
for i in range(1, root + 1):
    if root % i == 0:
        c += 1

if c == 2:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")