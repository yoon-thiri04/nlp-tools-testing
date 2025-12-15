import re

# Extrating capitalized words from a given string

text = "Hello learning Data Science is Fun"
pattern = r'\b[A-Z][a-z]*\b'

matches = re.findall(pattern,text)
print(matches)