n,m=map(int,input().split())
flag=False
for i in range(n):
    a,b,c=map(int,input().split())
    if (a+b+c)/3>=m:
        flag=True
if flag:
    print("Yes")
else:
    print("No")