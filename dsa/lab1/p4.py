n=int(input("Enter the size of the array"))
arr=[]
print ("Enter the elements")
for i in range(0,n):
	arr.append(int(input()))

a=arr[:]
b=arr[:]

for i in range(0,n-1):
	for j in range(0,n-i-1):
		if a[j]>a[j+1]:
			t=a[j]
			a[j]=a[j+1]
			a[j+1]=t
print ("Using bubble sort:")
for i in range(0,n):
	print(a[i])

for i in range(0,n-1):
	pos=i
	for j in range(i+1,n):
		if b[pos]>b[j]:
			pos=j
	if pos!=i:
		t=b[i]
		b[i]=a[pos]
		b[pos]=t
print ("Using selection sort:")
for i in range(0,n):
	print(a[i])
			


