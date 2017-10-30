x=int(input("Enter a number"))
c=0
if x==1:
	c=-1
	print("Neither True nor False")
else:
	for i in range(2,x):
		if x%i==0:
			c=c+1
if c==0:
	print ("True")
elif c>0:
	print ("False")
	