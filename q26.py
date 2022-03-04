list=[6,1,3,5,6,3,1]
i=0
a=[]
while i<len(list):
		if list[i] not in a:
			a.append (list[i])
		i+=1
j=0
b=1
while j<len(a):
	b=b*a[j]
	j+=1
print(a)
print(b)
#Op-90