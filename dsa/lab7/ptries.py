class Trienode:

	def __init__(self):
		self.children=[None for i in range(26)]
		self.end=False

class Trie:

	def __init__(self):
		self.root=self.get_node()

	def get_node(self):
		return Trienode()

	def insert(self,key):
		tmp=self.root
		k=list(key)
		for i in range(len(k)):
			index=ord(k[i])-ord('a')
			#print(index)
			if tmp.children[index]==None:
				tmp.children[index]=k[i]
				tmp.children[index]=self.get_node()
				tmp=tmp.children[index]
			else:
				tmp=tmp.children[index]
		tmp.end=True

	def search(self,key):
		tmp=self.root
		k=list(key)
		for i in range(len(k)):
			index=ord(k[i])-ord('a')
			if tmp.children[index]==None:
				return False
			else :
				tmp=tmp.children[index]
			#else:
				#tmp=tmp.children[index]
				return True

t=Trie()
t.insert("to")
t.insert("today")
t.insert("todat")
t.insert("toos")
t.insert("peach")
t.insert("act")
t.insert("action")
print(t.search("to"))
print(t.search("today"))
print(t.search("todat"))
print(t.search("toos"))
print(t.search("action"))
print(t.search("act"))
            




