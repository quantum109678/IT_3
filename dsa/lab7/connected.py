class Vertex:

	def __init__(self):
		self.dis=None
		self.colour='U'
		self.pred=None
		self.next=None

class node:

	def __init__(self,key):
		self.val=key
		self.next=None

def main():
	n=int(input("Enter the number of vertices:"))
	L=[]
	for i in range(n):
		L.append(Vertex())
	e=int(input("Enter the number of edges:"))
	print("Enter the edges:")
	for i in range(e):
		v1,v2=input().split()
		v1,v2=int(v1),int(v2)
		N1=node(v1)
		N2=node(v2)

		if L[v1]==None:
			L[v1]=N2
		else:
			tmp=L[v1].next
			L[v1].next=N2
			N2.next=tmp

		if L[v2]==None:
			L[v2]=N1
		else:
			tmp=L[v2].next
			L[v2].next=N1
			N1.next=tmp
	for i in range(n):
		if L[i].colour=='U':
			BFS(L,i)

def BFS(G,S):
	G[S].dis=0
	G[S].colour='F'
	Q=[]
	Q.append(S)
	while len(Q)!=0:
		u=int(Q.pop(0))
		tmp=G[u].next
		while tmp!=None:
			if G[tmp.val].colour=='U':
				G[tmp.val].dis=G[u].dis+1
				G[tmp.val].colour='F'
				G[tmp.val].pred=u
				Q.append(tmp.val)
			tmp=tmp.next
		G[u].colour='B'
	print("Vertices of connected components:")
	for i in range(len(G)):
		if G[i].colour=='B':
			print(i)
			G[i].colour='D'
		#print()


if __name__ == '__main__':
	main()

