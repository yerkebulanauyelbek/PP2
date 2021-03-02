n=int(input())
h=(n//3600)%24
m=n//60%60
s=n%60
xm=str(m)
xs=str(s)
if len(xs)<2:
    xs="0"+xs
if len(xm)<2:
    xm="0"+xm
print(h,xm,xs,sep=':')