class BinaryHeap:

	def __init__(self,n,D):
		self.A=[None for i in range(n+1)]
		for i in range(n):
			self.A[i+1]=D[i]
		for i in range(n//2,0,-1):
			self.heapify(n,i)

	def heapify(self,n,i):
		
		#print(n)
		l=2*i
		#print(l)
		r=2*i+1
		#print(r)
		largest=i
		if l<=n:
			if self.A[l]>self.A[i]:
				largest=l
		if r<=n:
			if self.A[r]>self.A[largest]:
				largest=r
		if largest!=i:
			tmp=self.A[largest]
			self.A[largest]=self.A[i]
			self.A[i]=tmp
			self.heapify(n,largest)


	def printHeap(self):
		for i in range(1,len(self.A)):
			print(self.A[i],end=" ")

	def maximum(self):
		return self.A[1]

	def extractmax(self):
		n=len(self.A)
		r=self.A[1]
		s=self.A[n-1]
		self.A[1]=s
		self.A[n-1]=r
		self.A.pop()
		for i in range (len(self.A)//2,0,-1):
			self.heapify(n,i)
		return r

	


def main():
	n=int(input("Enter number of elements"))
	D=[0 for i in range(n)]
	for i in range(n):
		D[i]=int(input("Enter the element"))
	H=BinaryHeap(n,D)

	for i in range(n-1,1,-1):
		H.A[i],H.A[1]=H.A[1],H.A[i]
		H.heapify(i,1)
	H.printHeap()



if __name__ == '__main__':
	main()