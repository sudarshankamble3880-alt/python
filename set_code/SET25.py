user1 = {"Amit", "Rahul", "Sneha", "Priya", "Kiran"}
user2 = {"Sneha", "Priya", "Rohan", "Neha", "Kiran"}

print("Mutual friends:", user1 & user2)
print("User 1 only:", user1 - user2)
print("User 2 only:", user2 - user1)
print("Total unique friends:", user1 | user2)
