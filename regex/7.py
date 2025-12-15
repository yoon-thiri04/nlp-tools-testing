import re

# in format vX.X.X 

text = "Versions: v1.2.3, v2.0.3, v4.1.10"
pattern  =r'\bv\d+\.\d+\.\d+\b'
matches = re.findall(pattern,text)

print(matches)