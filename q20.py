#output=[['a',6],['n', 3],['t',2],['x',2],['u',1],['g',1]]
ch= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
b=[]
while i<len(ch):
	j=0
	d=[]
	c=0
	while j<len(ch):
		if ch[i]==ch[j]:
			c+=1
		j+=1
	d.append(ch[i])
	d.append(c)
	if d not in b:
		b.append(d)
	i+=1
print(b)