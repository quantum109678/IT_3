import math

class BinaryHeap:
	def __init__(self):
		self.A=[None]

	def insert(self,x,t):
		self.A.append(x)
		p=t
		while True:
			q=p//2
			if q==0:
				break
			if self.A[p]>self.A[q]:
				tem=self.A[p]
				self.A[p]=self.A[q]
				self.A[q]=tem
				#swap(self.A[p],self.A[q])
				p=q
				q=p//2
			else:
				break	


	def maximum(self):
		return self.A[1]

	def extractMax(self):
		var=self.A[1]
		self.A[1]=self.A[len(self.A)-1]
		ret=self.A.pop()
		self.heapify(1)
		return var


	def heapify(self,i):
		while i<len(self.A)//2:
			child1=self.A[2*i]
			child2=self.A[2*i+1]
			value=max(child1,child2)
			if value>self.A[i]:
				if value==child1:
					t=self.A[i]
					self.A[i]=self.A[2*i]
					self.A[2*i]=t
					i=2*i
				else:
					t=self.A[i]
					self.A[i]=self.A[2*i+1]
					self.A[2*i+1]=t
					i=2*i+1
				c=len(self.A)
				if 2*i+1>=len(self.A):
					break
				else:
					child1=self.A[2*i]
					child2=self.A[2*i+1]


	def buildHeap(self,l):
		p = len(l) + 1
		m = [None] * p
		a = 0
		for i in range(1,p):
			b = a + 1
			m[b] = l[a]
			a = a + 1
		j = a
		for i in range(a):
			p = j
			while True:
				b = p//2
				if b != 0 :
					#print(m[b], m[p])
					if m[b] < m[p]:
						temp = m[b]
						m[b] = m[p]
						m[p] = temp
						p = b
						if b == 1:
							j = j + 1
					else:
						break
				else:
					break
			j = j - 1

		print(m)




"""def swap(a,b):
	t=a
	a=b
	b=t"""




def main():
	heap=BinaryHeap()
	s=int(input("Enter the size:"))
	t=1
	for i in range(s):
		ele=int(input("Enter the element: "))
		heap.insert(ele,t)
		t+=1
	for i in range(1,s+1):
		print(heap.A[i],end=' ')
	

	
		#print(B[2])
	"""heapify(B,1)
	print(B)"""
	print("Maximum:")
	print(heap.maximum())
	
	print("Extract maximum:")
	print(heap.extractMax())
	print("Heap after extracting maximum:")
	for i in range(1,s):
		print(heap.A[i],end=' ')

if __name__ == '__main__':
	main()