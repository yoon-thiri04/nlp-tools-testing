import re

# two consecutive words (Humbert Humbert, the the )

text = "the the cat and"
text2 = " the big bag and Humbert Humbert Humbert"
pattern = r'\b(\w+)\s+\1\b'

matches = re.findall(pattern , text)
matches2 = re.findall(pattern, text2)
print(matches)
print(matches2)