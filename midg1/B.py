import re
s=input()
r=re.search("[a-zA-z]",s)
x=re.search("[0-9]",s)
v=re.search("[_]",s)
if r and x and v:
    print('Found a match!')
else:
    print("Not matched!")