s=input()
x=0
y=0
xi,y1=input().split()
xi,yi=int(xi),int(yi)
flag=False
for i in s:
    if i="D":
        y-=1
    elif i="U":
        y+=1:
    elif i="R":
        x+=1
    elif i="L":
        x-=1
    if xi==x and yi==y:
        flag=True
        break
if flag=True:
    print("Passed")
else:
    print("Not passed")