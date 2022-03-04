Report card 2marks=[[78,76,95,86,88],[91,71,98,65],[95,45,78]]
i=0
sum=0
while i<len(marks):
	j=0
	sum1=0
	while j<len(marks[i]):
		sum1=sum1+marks[i][j]
		j=j+1
		sum1=sum+sum1
		over=sum1//len(marks[i])
	i+=1
	print("avarage of ",1+i,"year",over)