import re
post = input("Enter a post: ")
# Matches '#' followed by letters or digits
hashtags = re.findall(r'#\w+', post)
print("Hashtags:", hashtags)
