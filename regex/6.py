import re

#Validate passwords -> one uppercase/lowercase/digit/special character -> 8 character long

passwords = ["Ucsy@2025","hi123","newP$#22","12345678","betteroption$"]
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
for pwd in passwords:
    if re.match(pattern,pwd):
        print(pwd,"- Valid")
    else:
        print(pwd,"- Invalid")