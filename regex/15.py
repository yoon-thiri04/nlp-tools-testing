import re

# strings contain grotto and raven but not grottos 

texts = ["the raven lives in a dark grotto","the grottos and raven"]
pattern = r'\b(grotoo\b.*\braven|raven\b.*\bgrotto)\b'
for text in texts:
    print(text,"-",bool(re.search(pattern,text)))