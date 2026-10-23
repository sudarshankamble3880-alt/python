import re
phone = input("Enter a 10-digit mobile number: ")
# Indian numbers start with 6, 7, 8, or 9 followed by exactly 9 digits
if re.match(r'^[6-9]\d{9}$', phone):
    print("Valid Indian Mobile Number")
else:
    print("Invalid Mobile Number")
