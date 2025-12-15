import re

# time entries in the format HH:MM AM/PM -> 10:30 AM

text ="School starts at 09:49 AM and lunch at 12:30 PM .  "
pattern = r'\b(0[1-9]|1[0-2]):[0-5][0-9]\s?(AM|PM)\b'

matches = re.findall(pattern,text)
print(matches)

full= re.finditer(pattern,text)
print([m.group() for m in full])