import pandas as pd

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    grade = input("Enter the Grade: ")

    students.append([name, marks, grade])


df = pd.DataFrame(students, columns=["Name", "Marks", "Grade"])

df.to_csv("data.csv", index=False)

topper = df.loc[df["Marks"].idxmax()]

print("\nTopper:")
print("Name:", topper["Name"])
print("Marks:", topper["Marks"])
print("Grade:", topper["Grade"])
