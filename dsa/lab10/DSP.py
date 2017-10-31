class Vertex:


	def __init__(self,k):
		self.dis=20000
		self.key=k
		self.next=None

class Edge:

	def __init__(self,v1,v2,w):
		self.e1=v1
		self.e2=v2
		self.wei=w

class Node:

	def __init__(self,k):
		self.val=k
		self.next=None

L=[]
E=[]



def main():
	n=int(input("Enter number of vertices:"))
	for i in range(n):
		L.append(Vertex(i))
	#M=[[0 for i in range(0,n)]for j in range(0,n)]
	e=int(input("Enter number of edges:"))
	print("Enter the edges in the fotrmat \"Endpoint1 Endpoint2 Distance\":")
	for i in range(0,e):
		v1,v2,w=input().split()
		v1,v2,w=int(v1),int(v2),int(w)
		
		N1=Node(v1)

		N2=Node(v2)
		E.append(Edge(v1,v2,w))
		if L[v1].next==None:
			L[v1].next=N2
		else:
			tmp=L[v1].next
			N2.next=tmp
			L[v1].next=N2
			
		if L[v2].next==None:
			L[v2].next=N1
		else:
			tmp=L[v2].next
			N1.next=tmp
			L[v2].next=N1
	s=int(input("Enter the source vertex:"))
	DSP(L,E,s)

def DSP(L,E,s):
	L[s].dis=0
	H=MinHeap()
	for i in range(len(L)):
		H.insert(L[i])
	while len(H)!=0:
		w=H.extractMin()
		tmp=L[w].next
		while tmp!=None:
			for i in range(len(E)):
				if (E[i].e1==w.key and E[i].e2==tmp.val) or (E[i].e2==w.key and E[i].e1==tmp.val):
					cd=E[i].wei
			if w.dis+cd<L[tmp.val].dis:
				L[tmp.val]=w.dis+cd
			H.updatePrio(L[tmp.val])
