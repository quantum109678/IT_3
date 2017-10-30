class TreeNode:

	def __init__(self):
		self.left=None
		self.right=None
		self.key=None
		self.parent=None

class B_S_T:
	def __init__(self):
		self.root=None


	def insert(self,key,root):
		tmp=TreeNode()
		tmp.key=key
		self.insert_key(tmp,root)


	def insert_key(self,node,root):
		if root == None:
			self.root=node
		elif root.key>node.key:
			if root.left==None:
				root.left=node
				node.parent=root

			else:
				self.insert_key(node,root.left)

		else:
			if root.right==None:
				root.right=node
				node.parent=root
			else:
				self.insert_key(node,root.right)

	def minimum(self,root):
		if root==None: 
			return ("Empty tree")
		elif root.left==None:
			return root.key
		else:
			return self.minimum(root.left)

	def maximum(self,root):
		if root==None: 
			return ("Empty tree")
		elif root.right==None:
			return root.key
		else:
			return self.maximum(root.right)

	def search(self,root,key):
		if root==None:
			return("Element not found")
		elif root.key==key:
			return root
		elif root.key<key:
			return self.search(root.right,key)
		else:
			return self.search(root.left,key)

	def successor(self,x):
		root=self.search(self.root,x)
		if root==None or (root.right==None and root.left!=None):
			return("No sucessor")
		elif root.right==None and root.left==None:
			if root.parent.left==root:
				return root.parent.key
			else:
				return("No successor")
		else:
			root=root.right
			while root.left!=None:
				root=root.left
			return root.key

	def predecessor(self,x):
		root=self.search(self.root,x)
		if root==None or (root.left==None and root.right!=None):
			return("No predecessor")
		elif root.right==None and root.left==None:
			if root.parent.right==root:
				return root.parent.key
			else:
				return("No predecessor")
		else:
			root=root.left
			while root.right!=None:
				root=root.right
			return root.key

	def delete(self,k,root):
		y=self.search(root,k)
		if y.left==None and y.right==None:
			if y.parent.left==y:
				y.parent.left=None
			else:
				y.parent.right=None
		elif y.left!=None and y.right==None:
			if y.parent.left==y:
				x=y.parent
				y.parent.left=y.left
				y.left.parent=x
			else:
				x=y.parent
				y.parent.right=y.left
				y.left.parent=x
		elif y.left==None and y.right!=None:
			if y.parent.left==y:
				x=y.parent
				y.parent.left=y.right
				y.right.parent=x
			else:
				x=y.parent
				y.parent.right=y.left
				y.right.parent=x
		elif y.left!=None and y.right!=None:
			x=self.successor(root)
			y.key=x
			self.delete(x,root)

	def preorder(self,root):
		if root==None:
			return
		else:
			print(root.key)
			self.preorder(root.left)
			self.preorder(root.right)

def main():
	B=B_S_T()
	B.insert(10,B.root)
	B.insert(5,B.root)
	B.insert(3,B.root)
	B.insert(8,B.root)
	B.insert(6,B.root)
	B.insert(7,B.root)
	B.insert(14,B.root)
	B.insert(11,B.root)
	print("Minimum:")
	print(B.minimum(B.root))
	print("Maximum:")
	print(B.maximum(B.root))
	print("search for 11:")
	print(B.search(B.root,11))
	print("Predecessor of 10:")
	print(B.predecessor(10))
	print("Successor of 10:")
	print(B.successor(10))
	print("Preorder:")
	B.preorder(B.root)    
	B.delete(8,B.root)
	print("Preorder:")
	B.preorder(B.root)
	B.insert(13,B.root)
	




if __name__ == '__main__':
	main()