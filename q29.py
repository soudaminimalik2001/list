len=int(input('enter length'))
x=[ ]
j=0
while j<len:
	a=int(input('enter element'))
	x.append(a)
	j+=1
print(x)
i=0
min=x[i]
while i<j:
	if x[i]<min:
		min=x[i]
	i+=1
print(min)
#Minimum value with user