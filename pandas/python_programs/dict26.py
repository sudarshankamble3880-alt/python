# 26. Create a dictionary containing employee names and salaries.
# Find highest salary, lowest salary, average salary and employees
# earning more than Rs. 50,000.

employees = {
    "Amit": 45000,
    "Rahul": 60000,
    "Sneha": 75000,
    "Priya": 50000,
    "Rohan": 80000
}

print("Highest salary:", max(employees.values()))
print("Lowest salary:", min(employees.values()))

average = sum(employees.values()) / len(employees)
print("Average salary:", average)

print("Employees earning more than 50000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)
