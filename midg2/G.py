import re
txt=input()
t=input()
s=input()
f=input()
txt=re.sub(t,s,txt)
x = re.findall(f,txt)
print (len(x))