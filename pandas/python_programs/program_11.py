import pandas as pd

ages = {"P001": 65, "P002": 45, "P003": 72, "P004": 30, "P005": 68}
s = pd.Series(ages)

print("Average age:", s.mean())
print("Oldest patient:", s.idxmax(), s.max())
print("Youngest patient:", s.idxmin(), s.min())
print("\nPatients above 60:")
print(s[s > 60])
