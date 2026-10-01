import pandas as pd

salaries = {"Amit": 55000, "Neha": 48000, "Rahul": 62000, "Priya": 75000, "Sneha": 51000}
s = pd.Series(salaries)

print(s)
print("Highest salary:", s.max())
print("Lowest salary:", s.min())
print("Average salary:", s.mean())
print("\nEmployees earning more than 50000:")
print(s[s > 50000])
