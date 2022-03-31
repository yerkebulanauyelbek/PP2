a = int(input())
for i in range(10**a,(10**(a-1))-1,-1):
    if i%2!=0:
        print(i, end=' ')