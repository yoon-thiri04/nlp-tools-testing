import re

# conversion of the date yyyy-mm-dd to dd-mm-yyy format

date = "2025-12-05"
pattern = r'(\d{4})-(\d{2})-(\d{2})'

new_date = re.sub(pattern , r'\3-\2-\1', date)

print("Original Date:",date)
print("Converted Date:",new_date)
