import re
password = input("Enter a password: ")
# Lookaheads checking length (8+), 1 upper, 1 lower, 1 digit, 1 special character
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$'
if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password (Must have 8+ chars, 1 upper, 1 lower, 1 digit, 1 special)")
