n=int(input())
a=list(map(str,input().split()))
k=int(input())
ans=""
ans1=""
for i in a[0:k]:
    ans+=i
for i in a[k:]:
    ans1+=i
print(ans)
print(ans1)
print(int(ans) * int(ans1))