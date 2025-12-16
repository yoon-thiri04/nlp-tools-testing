"""
Docstring for nlp.preprocessing.syllablebreak

- We can make segmentation with word level, char level, syllable breaking
- for syllable -> Finite State Model or Regex or building syllable dictionary list
- now with regex from https://github.com/ye-kyaw-thu/myWord, the method is proposed in 2014.
"""

import re

myConsonant = r"က-အ" # basic burmese char
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္' # subscript symbols - က္က, တ္တ
aThat = r'်' # athat - က်,ပ်

# a consonant not after a subscript symbol AND a consonant is not followed by a-That character or a subscript symbol
# ?<! means -> NOT glued to the previous character - The character just before this consonant is NOT ္
# ?! means -> NOT glued to the next character -The character just after this consonant is NOT ် or ္

# ပါဌ်ဆင့် ဆင့်တဲ့ သင်္ကေတ နောက်က လိုက်တဲ့ ဗျည်း မဟုတ်ရင်၊ ပြီးတော့ အသတ်နဲ့တွဲနေတဲ့ ဗျည်း မဟုတ်ရင်
# အဲဒီဗျည်း စာလုံးရဲ့ ရှေ့မှာ break point လုပ်ပါ။ 
# သို့မဟုတ် အင်္ဂလိပ်စာလုံးတို့ otherChar အနေနဲ့ သတ်မှတ်ထားတဲ့ စာလုံးတွေ ဆိုရင်လည်း အဲဒီစာလုံးတွေရဲ့ ရှေ့မှာ break ထည့်ပါ
BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" 
                          + r"|[" + enChar + otherChar + r"])", re.UNICODE)

# Read the text 
with open("nlp/preprocessing/input.txt","r",encoding="utf-8") as f:
    text = f.read()

# Break syllable and insert | between
broke_text = BreakPattern.sub(r" \1",text)

# Remove leading |
# Write in output file
with open("nlp/preprocessing/output.txt","w", encoding="utf-8") as f:
    f.write(broke_text)