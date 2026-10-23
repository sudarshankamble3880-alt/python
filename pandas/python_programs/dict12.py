# 12. Create a dictionary containing student names and marks.
# Find the student with the lowest marks.

marks = {
    "Amit": 75,
    "Rahul": 90,
    "Sneha": 65,
    "Priya": 95
}

name = min(marks, key=marks.get)

print("Lowest marks:", name, marks[name])
