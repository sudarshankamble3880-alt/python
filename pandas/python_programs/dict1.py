# 1. Create a dictionary containing student details such as roll number, name, department, and marks.
# Display all key-value pairs.

student = {
    "roll": 101,
    "name": "Amit",
    "department": "Computer",
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)
