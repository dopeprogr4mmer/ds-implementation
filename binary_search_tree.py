"""
Implementation of Binary Tree
"""

class Node:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

	def is_empty(self):
		if not self.value and not self.right and not self.left:
			return True
		return False

	def is_leaf(self):
		if not self.right and not self.left:
			return True
		return False

	def make_empty(self):
		self.value = None
		self.left = None
		self.right = None

	def copy_right(self):
		self.value = self.right.value
		self.left = self.right.left
		self.right = self.right.right


class BST:
	def __init__(self, value=None):
		if value:
			newnode = Node(value)
			self.root = newnode
		else:
			self.root = value

	def min_val(self, node):
		if not node.left:
			return self.value
		return self.min_val(node.left)

	def copy_max_and_delete(self, node, parent, child="left"):
		if not node.right:
			print("max_val:", node.value)
			value = node.value
			if child == "left":
				parent.left = None
			else:
				parent.right = None
			return value
		else:
			return self.copy_max_and_delete(node.right, node, child="right")

	def find(self, value, node=1):
		if node == 1:
			node = self.root
		if not node:
			print(f"Element {value} not in tree")
			return False
		if node.value == value:
			return True
		if value < node.value:
			return self.find(value, node.left)
		else:
			return self.find(value, node.right)

	def insert(self, value):
		if not self.root:
			newnode = Node(value)
			self.root = newnode
			print(f"Element {value} inserted to binary tree")
			return True
		curr_node = self.root
		parent_node = None
		child = None
		while True:
			if not curr_node:
				newnode = Node(value)
				if child == "left":
					parent_node.left = newnode
				else:
					parent_node.right = newnode
				print(f"Element {value} inserted to binary tree")
				return True
			if curr_node.value == value:
				print("Element already present")
				return False
			parent_node = curr_node
			if value < curr_node.value:
				curr_node = curr_node.left
				child = "left"
			else:
				curr_node = curr_node.right
				child = "right"

	def delete(self, value):
		if not self.root:
			print("Empty Tree")
			return False
		if not self.find(value):
			return False
		curr_node = self.root 
		parent_node = None
		child = None
		while True:
			if value == curr_node.value:
				if curr_node.is_leaf():
					if parent_node:
						if child == "left":
							parent_node.left = None
						else:
							parent_node.right = None
					else:
						self.root = None
					print(f"Element {value} deleted from  tree")
					return True
				elif not curr_node.left:
					curr_node.copy_right()
					print(f"Element {value} deleted from  tree")
					return True
				else: 
					curr_node.value = self.copy_max_and_delete(curr_node.left, curr_node)
					#self.delete(self.max_val(curr_node.left))
					print(f"Element {value} deleted from  tree")
					return True
			parent_node = curr_node
			if value < curr_node.value:
				curr_node = curr_node.left
				child = "left"
			else:
				curr_node = curr_node.right
				child = "right"

	def inorder(self, node=1):
		if node == 1:
			node = self.root
		if not node:
			return []
		return self.inorder(node.left) + [node.value] + self.inorder(node.right)

	def __str__(self):
		return str(self.inorder())

if __name__ == '__main__':
	t = BST()
	t.insert(50) 
	t.insert(30)
	t.insert(80)
	t.insert(70)
	t.insert(90)
	t.insert(85)
	t.insert(95)
	t.find(5)
	
	t = BST(7)
	t.insert(2)
	t.insert(4)
	t.insert(5)
	t.insert(3)
	t.insert(11)
	t.insert(8)
	print(t)
	t.delete(21)
	t.delete(7)
	print(t)
	t.delete(11)
	print(t)