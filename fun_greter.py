#3.	Define a function that accepts two numbers and returns the greater number.

def find_greater(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2


print('Greater number is',find_greater(5,10))
