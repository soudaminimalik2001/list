#Substring nikalo
mainstr="the quick broun for fumhed over the lezy dog the dog split over the verandah"
substr="over"
replacementstr="on"
ss="over"
i=0
k=" "
s=mainstr.split()
while i<len(s):
	if s[i]==ss:
		k=k+"on"
	else:
		k=k+" "+s[i]
	i=i+1
 print(k)