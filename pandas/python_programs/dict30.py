# 30. Take a dictionary containing student names and departments.
# Create a new dictionary that groups students according to their department.

students = {
    "Amit": "Computer",
    "Rahul": "IT",
    "Sneha": "Computer",
    "Priya": "ENTC",
    "Rohan": "IT"
}

groups = {}

for name, dept in students.items():
    if dept not in groups:
        groups[dept] = []
    groups[dept].append(name)

print(groups)
