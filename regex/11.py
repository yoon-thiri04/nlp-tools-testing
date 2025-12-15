import re

# strings start line integer and end line with a word

strings = ["123 hello hello", "when I was young","4. Fill the blank","hello 1234"]

pattern = r'^\d+.*[A-Za-z]+$'

for string in strings:
    print(string,bool(re.match(pattern,string)))