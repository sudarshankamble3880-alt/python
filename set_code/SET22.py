e1 = {"Python", "Java", "SQL", "Git", "HTML"}
e2 = {"Python", "C++", "SQL", "Docker", "Git"}

print("Common skills:", e1 & e2)
print("Employee 1 only:", e1 - e2)
print("Employee 2 only:", e2 - e1)
print("All skills:", e1 | e2)
