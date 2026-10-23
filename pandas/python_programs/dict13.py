# 13. Create a dictionary containing student names and marks.
# Calculate the average marks of all students.

marks = {
    "Amit": 75,
    "Rahul": 90,
    "Sneha": 85,
    "Priya": 95
}

total = sum(marks.values())
average = total / len(marks)

print("Average marks:", average)
