n=int(input())
k=int(input())
res1=1
res2=1
res3=1
for i in range(1,n+1):
    res1*=i
for x in range(1,k+1):
    res2*=x
for j in range(1,n-k+1):
    res3*=j
print(int((res1)/(res2*res3)))