subject=int(input())
subject=subject*45+(subject//2)*5+((subject+1)//2-1)*15
print(subject//60+9, subject%60)