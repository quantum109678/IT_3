s1=input("Enter String1")
s2=input("Enter String2")
s3=input("Enter String3")

l=len(s2)
n=len(s1)
for i in range(0,n,l+1):
	a=s1[i:i+l]
	if a==s2:
		s1=s1.replace(s2,s3)
print (s1)






