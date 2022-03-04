a=['pu_ja','li_za']
i=0
b=[]
while i<len(a):
	j=0
	str=' '
	while j<len(a[i]):
		if a[i][j]=='_':
			pass
		else:
			str+=a[i][j]
		#b.append(a[i][j])
		j+=1
	b.append(str)
	i+=1
print(b)
#o/p-['puja','liza']