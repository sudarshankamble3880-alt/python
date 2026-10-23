# 6. Create a dictionary of employee IDs and names.
# Ask the user for an employee ID and check whether it exists.

employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha",
    104: "Priya"
}

id = int(input("Enter employee ID: "))

if id in employees:
    print("Employee exists")
else:
    print("Employee does not exist")
