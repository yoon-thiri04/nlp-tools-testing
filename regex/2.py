import re

# Words containing "ing"

text = "I am running and singing while thinking. You make my feeling worst."
pattern = r'\b\w*ing\w*\b'

matches = re.findall(pattern, text)
print(matches)