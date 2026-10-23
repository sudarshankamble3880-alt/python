# 11. Create a dictionary containing student names and marks.
# Find the student who has scored the highest marks.

marks = {
    "Amit": 75,
    "Rahul": 90,
    "Sneha": 85,
    "Priya": 95
}

name = max(marks, key=marks.get)

print("Highest marks:", name, marks[name])
