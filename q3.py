n= [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
max2=0
while i<len(n):
	if max<n[i]:
		max=n[i]
	if max2<n[i]<max:
		max2=n[i]
	i+=1
print(max2)
Second maximum number