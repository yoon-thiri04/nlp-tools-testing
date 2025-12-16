from myword import SyllableTokenizer,WordTokenizer

text = "ကျွန်တော်ကသုတေသနသမားပါ။ နေ့ရောညရောမြန်မာစာနဲ့ကွန်ပျူတာနဲ့ပဲအလုပ် များ ပါ တယ်"

#syltok = SyllableTokenizer()
#print(syltok.tokenize(text))

wordtok = WordTokenizer()
tokenize= wordtok.tokenize(text)

line=" ".join(tokenize)
with open("D:/python_hand_face_testing/nlp/preprocessing/word_output.txt","w",encoding="utf-8") as f:
    f.write(line)