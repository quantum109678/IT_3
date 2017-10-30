class Vertex:


	def __init__(self):
		self.dis=None
		self.colour=U
		self.pred=None



def main():
	n=int(input("Enter number of vertices:"))
	L=[]
	q=[]
	for i in range(0,n):
		L[i]=Vertex()
	M=[[0 for i in range(0,n)]for j in range(0,n)]
	e=int(input("Enter number of edges:"))
	print("Enter the edges:")
	for i in range(0,e):
		v1,v2=input().split()
		v1,v2=int(v1),int(v2)
		M[v1][v2]=1
		M[v2][v1]=1	
	s=int(input("Enter source vertex"))
	L[s].dis=0
	L[s].colour=F
	q.append(L[s])
	while size(q)!=0:
		u=q.pop(0)
	print(u)
	





if __name__ == '__main__':
	main()