s=input()
s1=s.split(" ")
max1=-1
sl=""
for i in s1:
    if len(i)>max1:
        max1=len(i)
        sl=i
print(sl)
print(max1)