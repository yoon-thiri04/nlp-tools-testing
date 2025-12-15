import string

# Step 1: Open the text file
file = open("D:/python_hand_face_testing/nlp/text.txt", "r", encoding="utf-8")
text = file.read()
file.close()

text = text.lower()
pattern = ''
text = text.translate(str.maketrans("", "", string.punctuation))


words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


for word in word_count:
    print(word, ":", word_count[word])