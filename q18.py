Total sum
n=[10,11,12,13,14,17,18,19]
i=0
a1=[]
while i<len(n):
	k=i
	a2=[]
	while k<len(n):
		m=n[i]+n[k]
		if m==30:
			a2.append(n[i])
			a2.append(n[k])
			a1.append(a2)
		k=k+1
	i=i+1
	print(a1)