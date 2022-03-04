a=[4,5,[5,2],[6,2],8,9]
i=0
sum=0
b=' '
x=[]
while i<len(a):
	if type(a[i])==int:
		x.append(a[i])
	elif type(a[i])==list:
		j=0
		while j<len(a[i]):
			sum=sum+a[i][j]
			j+=1
	i+=1
print(sum)
x.insert(2,[sum])
print(x)
#O/p-5+2+6+2=15
#X=[4,5,[15],8,9]