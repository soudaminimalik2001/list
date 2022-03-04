x= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
num=0
while i<len(x):
	if x[i]%2==0:
		sum=sum+(x[i])
	if x[i]%2!=0:
		num=num+(x[i])
	i+=1
print('even',sum)
print('odd',num)