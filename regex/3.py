import re

text = "hello bookkeeper apple cool test loop happy dog"

full_words = [w for w in text.split() if re.search(r'(\w)\1', w)]

print(full_words)
