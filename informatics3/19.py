import math
a=int(input())
b=int(input())
c=int(input())
alpha = math.acos((b*b+c*c-a*a)/(2*b*c))
if (a*a)+(b*b)==c*c:
    print("rectengular")
elif a+b<=c or a+c<=b or b+c<=a or a+b+c<=0:
    print("impossible")
elif alpha < math.pi / 2:
    print('acute')
else:
    print('obtuse')