a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
max=0
c=0
while i<len(a):
	if len(a[i])>max:
		max=len(a[i])
		c=a[i]
	i+=1
print(max)
j=0
min=len(a[0])
while j<len(a):
	if len(a[j])<=min:
		min=len(a[j])
	j+=1
print(min)
#maximum and minimum in nested list