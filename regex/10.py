import re

# Starts and ends with vowel

text = "area idea and cake apple orange"
pattern = r'\b[aeiouAEIOU]\w*[aeiouAEIOU]\b'

matches = re.findall(pattern,text)
print(matches)