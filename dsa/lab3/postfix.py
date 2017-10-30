class Stack():
	def __init__(self):
		self.list=[]
		self.top=-1
	def push(self,x):
		self.list.append(x)
	def pop(self):
		return(self.list.pop())

def main():
	S=Stack();
	s='10 4 * 8 4 / +'
	l=s.split()
	for i in range(0,len(l)):
		if l[i]=='+': 
			op1=int(S.pop())
			op2=int(S.pop())
			res=op1+op2
			S.push(res)
		elif l[i]=='-':
			op1=int(S.pop())
			op2=int(S.pop())
			res=op2-op1
			S.push(res)
		elif l[i]=='*':
			op1=int(S.pop())
			op2=int(S.pop())
			res=op2*op1
			S.push(res)
		elif l[i]=='/':
			op1=int(S.pop())
			op2=int(S.pop())
			res=op2/op1
			S.push(res)
		else:
			S.push(l[i])
	fin=S.pop()
	print(fin)

if __name__ == '__main__':
	main()
