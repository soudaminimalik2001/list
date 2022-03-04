len=int(input('enter length'))
x=[ ]
j=0
while j<len:
	a=int(input('enter element'))
	x.append(a)
	j+=1
print(x)
i=0
max=0
while i<j:
	if max<x[i]:
		max=x[i]
	i+=1
print(max)
#Maximum number with user input