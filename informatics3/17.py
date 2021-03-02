a=int(input())
if 5<=a%10<=9 or a%10==0 or a//10==1:
    print(a,"korov")
elif a%10==1:
    print(a,"korova")
else:
    print(a,"korovy")