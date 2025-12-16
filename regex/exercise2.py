import re

# Myanmar unicode u1000-U+109F
# [^\u1000-\u109F\s]

with open("D:/python_hand_face_testing/nlp/regex/input.txt","r",encoding="utf-8") as f:
    text = f.read()


cleaned_text = re.sub(r'[^\u1000-\u109F\s]',"",text)

# removes extra spaces
cleaned_text= re.sub(r'\s+'," ",cleaned_text)

with open("D:/python_hand_face_testing/nlp/regex/output.txt","w",encoding="utf-8") as f:
    f.write(cleaned_text)

