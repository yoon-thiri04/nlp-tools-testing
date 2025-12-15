import re

# Match CSxx and CTxx - x is a single digit

text = "CS20 CS61 CT11 CT32 CS601"
pattern = r'\bC[ST]\d\d\b'

matches = re.findall(pattern,text)
print(matches)