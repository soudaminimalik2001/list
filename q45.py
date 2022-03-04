num=int(input("enter number"))
i=1
n=[]
while i<=num:
	m=[]
	j=1
	while j<=i:
		m.append(j)
		j=j+1
	if m==[1]:
		m=[ ]
	n.append(m)
	i=i+1
print(n)
#O/p-a=1 then it come []
#If a=2 then it come [[],[1,2]]