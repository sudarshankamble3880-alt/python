import pandas as pd

students = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Sneha"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
    "Total_Classes": [100, 100, 120, 90, 110],
    "Classes_Attended": [80, 70, 100, 60, 95]
}

df = pd.DataFrame(students)
df["Attendance_Percentage"] = df["Classes_Attended"] / df["Total_Classes"] * 100
print(df)
print("\nStudents below 75% attendance:")
print(df[df["Attendance_Percentage"] < 75])
