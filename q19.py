magi =[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(magi):
	j=0
	sum=0
	while j<len(magi[0]):
		sum=sum+magi[0][j]
		k=0
		sum1=0
		while k<len(magi[1]):
			sum1=sum1+magi[1][k]
			k1=0
			sum2=0
			while k1<len(magi[2]):
				sum2=sum2+magi[2][k1]
				k1=k1+1
			k=k+1
		j=j+1
	i=i+1
print (sum)
print (sum1)
print (sum2)

