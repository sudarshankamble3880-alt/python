morning = {"Amit", "Rahul", "Sneha", "Priya", "Rohan"}
afternoon = {"Sneha", "Priya", "Kiran", "Neha", "Rohan"}

print("Both:", morning & afternoon)
print("Morning only:", morning - afternoon)
print("Afternoon only:", afternoon - morning)
print("At least one:", morning | afternoon)
