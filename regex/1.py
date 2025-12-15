import re

text = "this is words like mango, cat, house, moon, elephant"

pattern = r'\b[a-zA-Z]{4,6}\b'
matches = re.findall(pattern, text)

print(matches)