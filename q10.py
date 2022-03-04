kph= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
while i<len(kph):
	if kph[i]>1000000 or kph[i]==1000000:
		print(kph[i],'crorepati')
	if kph[i]>100000 or kph[i]==100000:
		print(kph[i],'lakhpati')
	else:
		print(kph[i],'dilwale')
	i+=1