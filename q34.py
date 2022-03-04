a=[2,4,6,8]
i=-1
b=[ ]
while i>-len(a):
	c=a[i]-a[i-1]
	b.append(c)
	i-=1
print(b)
#O/p-[2,2,2]