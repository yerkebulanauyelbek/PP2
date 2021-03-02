a=int(input())
a1=str((a//100)//10)
a2=str((a//100)%10)
a3=str((a//10)%10)
a4=str(a%10)
if a1==a4 and a2==a3:
    print(1)
else:
    print(2)