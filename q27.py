a= [1, 2, 2, 5, 8, 4, 4, 8]
#op-Count = 5 #because [1,2,5,8,4] are unique values.
i=0
c=0
b=[]
while i<len(a):
	if a[i] not in b:
		b.append(a[i])
		c+=1
	i+=1
print(c)