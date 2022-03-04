a=[4,5,[5,2],[6,2],8,9]
i=0
sum=0
b=[]
x=[]
while i<len(a):
	if type(a[i])==int:
		x.append(a[i])
	elif type(a[i])==list:
			sum=a[2][0]+a[3][0]
			num=a[2][1]+a[3][1]
	i+=1
b.append(sum)
b.append(num)
print(b)
x.insert(2,b)
print(x)
o/p-5+6=11
2+2=4
b=[11,4]
x=[4,5,[11,4],8,9]