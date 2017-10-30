class Hashtable:

	def __init__(self):
		self.T=[None for i in range(30)]

	def insert(self,k):
		key=0
		for i in range(0,len(k)):
			key=key+ord(k[i:i+1])
		key=key%30
		
		tmp=ListNode()
		tmp.value=k
		
		if self.T[key]==None:
			self.T[key]=tmp
		else:
			tmp.next=self.T[key]
			self.T[key]=tmp
			


	def search(self,k):
		key=0
		flag=0
		c=0
		for i in range(0,len(k)):
			key=key+ord(k[i:i+1])
		key=key%30

		
		if self.T[key]==None:
			
			return ("False")
		else:
			tmp=self.T[key]
			while tmp.next!=None:
				if tmp.value==k:
					return("True")
				
				tmp=tmp.next
			if tmp.value==k:
				return("True")
			else:
				return("False")
			

	def keys(self):
		for i in range(0,30):
			if self.T[i]!=None:
				c=0
				tmp=self.T[i]

			
				while(tmp.next!=None):
					c=c+1
					tmp=tmp.next
				tmp=self.T[i]
				for j in range(0,c+1):
					print(tmp.value)
					tmp=tmp.next




class ListNode:
    def __init__(self):
        self.value=0
        self.next=None

def main():
	H=Hashtable()
	k="cat"
	m="act"
	H.insert(k)
	H.insert(m)
	print(H.search("act"))
	H.keys()
	H.insert("hgbdh")
	H.insert("oreo")
	H.insert("nmbvbsdh")
	print(H.search("oreo"))
	print(H.search("hgbdh"))
	H.keys()













if __name__ == '__main__':
	main()

