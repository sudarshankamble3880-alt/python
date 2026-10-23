# 25. Create a dictionary containing student names and marks.
# Add, update, delete, search, display, find highest marks and calculate average.

students = {
    "Amit": 80,
    "Rahul": 75,
    "Sneha": 90
}

students["Priya"] = 85
students["Rahul"] = 88

del students["Amit"]

name = "Sneha"

if name in students:
    print("Student found:", students[name])

print("All students:", students)

highest = max(students, key=students.get)
print("Highest marks:", highest, students[highest])

average = sum(students.values()) / len(students)
print("Average:", average)
