n=int(input())
a=list(map(int,input().split()))
a.sort()
x=set(a)
x=list(x)
for i in range(len(x)):
    print(i+1,x[i])
