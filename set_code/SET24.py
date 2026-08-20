day1 = {101, 102, 103, 104, 105}
day2 = {104, 105, 106, 107, 108}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("First day only:", day1 - day2)
print("Second day only:", day2 - day1)

category1 = {"Laptop", "Mouse", "Keyboard", "Monitor"}
category2 = {"Keyboard", "Monitor", "Printer", "Scanner"}

print("Common products:", category1 & category2)
