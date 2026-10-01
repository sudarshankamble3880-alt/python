import pandas as pd

students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Neha", "Rahul", "Priya", "Sneha"],
    "Python": [80, 72, 90, 65, 85],
    "DBMS": [75, 68, 88, 70, 82],
    "Mathematics": [82, 74, 91, 67, 86]
}

df = pd.DataFrame(students)
print(df)

df["Total"] = df[["Python", "DBMS", "Mathematics"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Mathematics"]].mean(axis=1)

print("\nTotal and Average:")
print(df[["Student_ID", "Student_Name", "Total", "Average"]])

print("\nStudents with average > 75:")
print(df[df["Average"] > 75])
