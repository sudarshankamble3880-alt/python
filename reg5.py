import re
# Use a multiline input or hardcoded text to demonstrate tabs/newlines easily
text = "Hello World\tTabs\nNewlines"
whitespace = re.findall(r'\s', text)
print("Identified whitespace characters:", whitespace)
