a=[1,2,3,[4,5,6],7,[8,9,10],11]
i=0
b=[]
c=[]
while i<len(a):
	j=1
	f=0
	if type(a[i])==int:
		while j<=a[i]:
			if a[i]%j==0:
				f+=1
			j+=1
		if f==2:
			b.append(a[i])
	elif type([i])==list:
		c=0
		while j<=a[i]:
			if a[i][c]%j==0:
				f+=1
			c+=1
		j+=1
		if f==2:
			b.append(a[i])
	else:
		c.append(a[i])
	i+=1
print(b,'prime number')
print(c,'not prime number')