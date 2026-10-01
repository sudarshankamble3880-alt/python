import pandas as pd

employees = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Amit", "Neha", "Rahul", "Priya", "Sneha"],
    "Department": ["CSE", "IT", "HR", "CSE", "IT"],
    "Salary": [55000, 48000, 62000, 75000, 51000],
    "Experience": [3, 2, 7, 10, 5]
}

df = pd.DataFrame(employees)
print(df[df["Salary"] > 50000])
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Employee with highest experience:")
print(df.loc[df["Experience"].idxmax()])
