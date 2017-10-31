class vertex:


	def __init__(self,k):
		self.val=k
		self.colour="W"
		self.pred=None
		self.dis=None
		self.next=None

class Node:


	def __init__(self,k):
		self.value=k
		self.next=None



def main():
	 n=int(input("Enter the number of vertices:"))
	 L=[]
	 for i in range(n):
	 	L.append(vertex(i))

	 e=int(input("Enter the number of edges:"))
	 print("Enter the edges:")
	 for i in range(0,e):
	 	v1,v2=input().split()
	 	v1,v2=int(v1),int(v2)
	 	N1=Node(v1)
	 	N2=Node(v2)
	 	if L[v1].next==None:
	 		L[v1].next=N2
	 	else:
	 		tmp=L[v1].next
	 		L[v1].next=N2
	 		N2.next=tmp

	 	if L[v2].next==None:
	 		L[v2].next=N1
	 	else:
	 		tmp=L[v2].next
	 		L[v2].next=N1
	 		N1.next=tmp
	 s=int(input("Enter source vertex:"))
	 bfs(L,s)
	 for i in range(n):
	 	print("Distance of ",i," from source ",s,":",L[i].dis)

def bfs(G,S):
	q=[0 for i in range(10)]
	G[S].dis=0
	G[S].colour="Y"
	q.append(S)
	while len(q)!=0:
		u=int(q.pop(0))
		tmp=G[u].next
		while tmp!=None:
			if G[tmp.value].colour=="W":
				G[tmp.value].dis=G[u].dis+1
				G[tmp.value].pred=u
				G[tmp.value].colour="Y"
				q.append(tmp.value)
			tmp=tmp.next
		G[u].colour="B"






if __name__ == '__main__':
	main()



