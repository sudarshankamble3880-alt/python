import re
text = input("Enter a string with URLs: ")
# http followed by an optional 's' and :// plus non-space characters
urls = re.findall(r'https?://\S+', text)
print("Web addresses:", urls)
