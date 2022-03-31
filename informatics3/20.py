n=int(input())
cnt3=n//60
cnt2=(n%60)//10
cnt1=n%10
if cnt1*15>125:
    cnt1=0
    cnt2+=1
if cnt1*15+cnt2*125>440:
    cnt1=0
    cnt2=0
    cnt3+=1
print(cnt1,cnt2,cnt3)