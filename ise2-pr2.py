def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2


num1 = int(input("Enter the num 1: "))
num2 = int(input("Enter the num 2: "))

print("\n1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")

ch1 = int(input("Enter the choice: "))

if ch1 == 1:
    print("Result:", add(num1, num2))

elif ch1 == 2:
    print("Result:", sub(num1, num2))

elif ch1 == 3:
    print("Result:", mul(num1, num2))

elif ch1 == 4:
    print("Result:", div(num1, num2))

