# college project packages

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from student.details import student_details
from student.marks import student_marks
from faculty.details import faculty_details

print(student_details())
print(student_marks())
print(faculty_details())