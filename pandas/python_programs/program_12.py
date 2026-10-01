import pandas as pd

attendance = {"Amit": 80, "Neha": 72, "Rahul": 95, "Priya": 65, "Sneha": 91}
s = pd.Series(attendance)

print("Average attendance:", s.mean())
print("\nBelow 75%:")
print(s[s < 75])
print("\nAbove 90%:")
print(s[s > 90])
print("\nHighest attendance:", s.max())
