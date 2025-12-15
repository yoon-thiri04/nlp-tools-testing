import re

# a,b such that a is preceded and followed by b -> bab

strings = ["bab","bbbabbb","aba","a","bbbabbbabb"]

pattern = r'^(b|bab)*$'
for string in strings:
    print(string, bool(re.match(pattern, string)))