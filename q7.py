i=0
while i<len(m):
	j=0
	sum=0
	while j<len(m[i]):
		sum=sum+m[i][j]
		avg=sum//len(m[i])
		j+=1
	i+=1
	print('avarage of ',0+i,'year',avg)
meraki report card part ll