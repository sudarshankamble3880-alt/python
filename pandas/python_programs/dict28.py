# 28. Create a dictionary containing names and phone numbers.
# Implement add, search, update, delete and display all contacts.

contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234",
    "Sneha": "9123456780"
}

contacts["Priya"] = "9988776655"

name = "Amit"

if name in contacts:
    print("Contact found:", contacts[name])

contacts["Amit"] = "9999999999"

del contacts["Rahul"]

print("All contacts:")

for name, number in contacts.items():
    print(name, ":", number)
