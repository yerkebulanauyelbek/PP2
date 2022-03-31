import re
s=input()
r=re.search("[A-Z][a-z]",s)
if r:
    print('Found a match!')
else:
    print("Not matched!")