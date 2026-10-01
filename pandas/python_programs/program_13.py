import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

subjects = ["Python", "DBMS", "Maths"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

print("\nTotal and average:")
print(df[["Student_ID", "Name", "Total", "Average"]])

print("\nStudents with average > 75:")
print(df[df["Average"] > 75])

print("\nStudent with highest average:")
print(df.loc[df["Average"].idxmax()])

print("\nAverage marks by subject:")
print(df[subjects].mean())
