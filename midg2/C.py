n=int(input())
a=list(map(int,input().split()))
x = set(a)
if len(a)==len(x):
    print("YES")
else:
    print("NO")