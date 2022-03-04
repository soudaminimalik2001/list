a=['a','b','c',['b','c'],['a','b','c']]
i=0
c=0
c1=0
c2=0
while i<len(a):
	j=0
	while j<len(a[i]):
		if a[i][j]=='a':
			c+=1
		if a[i][j]=='b':
			c1+=1
		if a[i][j]=='c':
			c2+=1
		j+=1
	i+=1
print('a',c)
print('b',c1)
print('c',c2)
O/p:-a 2
        b 3
        c 3