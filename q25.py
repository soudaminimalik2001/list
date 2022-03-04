#o/p:-gfgisbest
list=[['g','f','g'],['i','s'],['b','e','s','t']]
i=0
a=' '
while i<len(list):
	j=0
	while j<len(list[i]):
		a=a+list[i][j]
		j+=1
	i+=1
print(a)