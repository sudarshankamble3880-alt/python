import pandas as pd

marks = {"Amit": 80, "Neha": 72, "Rahul": 90, "Priya": 65, "Sneha": 85}
s = pd.Series(marks)

print(s)
print("\nAmit's marks:", s["Amit"])
print("Maximum:", s.max())
print("Minimum:", s.min())
print("Average:", s.mean())
print("\nStudents scoring more than 75:")
print(s[s > 75])
