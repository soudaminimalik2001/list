x= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=0
c1=0
#len=len(x[i])
sum=0
num=0
while i<len(x):
	if x[i]%2==0:
		sum=sum+(x[i])
		avg=sum/10
		c=c+1
	elif x[i]%2!=0:
		num=num+(x[i])
		avg1=num/10
		c1=c1+1
	i+=1
print(c)
print(c1)
print('even',sum)
print('even',avg)
print('odd',num)
print('odd',avg1)