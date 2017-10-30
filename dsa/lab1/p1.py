

def factorial(a):
	sum=1
	for i in range(1,a+1):
		sum=sum*i
	print (sum)

def fact(a):
	
	if(a>1):
		return a*fact(a-1)
	else:
		return 1
 	
a=int(input('Enter a positive integer'))
print ("Factorial using iteration")
factorial(a)
print ("Factorial using recursion")
print (fact(a))

