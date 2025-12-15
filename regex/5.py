import re

# All dates in Formats DD-MM-YYYY, DD/MM/YYYY , DD.MM.YYYY

text = "Dates: 12-05-2025, 30/04/2025, 10.12.2025, and 31:05:2025"
pattern =r'\b\d{2}[-/.]\d{2}[-/.]\d{4}\b'

matches = re.findall(pattern,text)
print(matches)