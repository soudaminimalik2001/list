a=[[8,3,4],[1,5,9],[6,7,2]]
print(len(a))
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
d1=0
d2=0
i=0
while i<len(a):
    r1=r1+a[0][i]
    r2=r2+a[1][i]
    r3=r3+a[2][i]
    c1=c1+a[i][0]
    c2=c2+a[i][1]
    c3=c3+a[i][2]
    d1=d1+a[i][0]
    d2=d2+a[i][1]
    i+=1
#print(r1)
#print(r2)
print(r3)
#print(c1)
#print(c2)
print(c3)
#print(d1)
print(d2)
if r1==r2==r3==c1==c2==c3==d1==d2:
    print("magic square")
else:
    print("not a magic square")