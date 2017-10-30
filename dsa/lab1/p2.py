def fibo1(i):
	if(i==0):
		return 0
	elif(i==1):
		return 1
	else:
		return fibo1(i-2)+fibo1(i-1)
 
def fibo2(n):
 	t1=0
 	t2=1
 	c=2
 	if n>=1:
 		print (t1)
 	if n>=2:
 		print (t2)
 	
 	while c<n:
 		xt=t1+t2
 		c=c+1
 		print(xt)
 		t1=t2
 		t2=xt

n=int(input("Enter n"))
print ("Using recursion")
for i in range(0,n):
	print (fibo1(i))
print ("Using iteration")
fibo2(n)