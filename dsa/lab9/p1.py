
class Node:

	def __init__(self,k):
		self.val=k
		self.next=None






def main():
	n=int(input("Enter number of vertices:"))
	L=[None for i in range(0,n)]
	M=[[0 for i in range(0,n)]for j in range(0,n)]
	e=int(input("Enter number of edges:"))
	print("Enter the edges:")
	for i in range(0,e):
		v1,v2=input().split()
		v1,v2=int(v1),int(v2)
		
		N1=Node(v1)

		N2=Node(v2)
		if L[v1]==None:
			L[v1]=N2
		else:
			tmp=L[v1]
			N2.next=tmp
			L[v1]=N2
			
		if L[v2]==None:
			L[v2]=N1
		else:
			tmp=L[v2]
			N1.next=tmp
			L[v2]=N1
		M[v1][v2]=1
		M[v2][v1]=1
	print("Adjacency matrix:")
	for i in range(0,n):
		for j in range(0,n):
			print(M[i][j],end=' ')
		print()
	print("Adjacency list:")
	for i in range(0,n):
		if L[i]==None:
			continue
		else:
			print("Vertex",i,end=':')
			tmp=L[i]
			while tmp!=None:
				print(tmp.val,end=' ')
				tmp=tmp.next
			print()

if __name__ == '__main__':
	main()

