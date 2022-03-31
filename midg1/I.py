n=int(input())
a=list(map(int,input().split()))
x=set(a)
x=list(x)
if a==x:
    print("Interesting")
else:
    print("Not interesting")