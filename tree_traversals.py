from binary_search_tree import BST
from collections import deque

#Flatten BST to sorted list
def inorder(root):
	if not root:
		return []
	else:
		return (inorder(root.left) + [root.value] + inorder(root.right))

def preorder(root):
	if not root:
		return []
	else:
		return ([root.value] + preorder(root.left) + preorder(root.right))

def postorder(root):
	if not root:
		return []
	else:
		return (postorder(root.left) + postorder(root.right) + [root.value])

def levelorder(root):
	q = deque()
	if not root:
		return []
	else:
		q.append(root)
	level_order = []
	while q:
		node = q.popleft()
		level_order.append(node.value)
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
	return level_order

def levelorder_recursive(root, q=deque(), level_order=[]):
	if not root:
		return level_order
	level_order.append(root.value)
	if root.left:
		q.append(root.left)
	if root.right:
		q.append(root.right)
	node = q.popleft() if q else None
	return levelorder_recursive(node, q, level_order)

def verticalorder(root):
	if not root:
		return []
	order_dict = {}
	vertical_order = []
	q = deque()
	delta, nx, px = 0, 0, 0
	q.append((root, delta))
	while q:
		node, delta = q.popleft()
		if delta in order_dict:
			order_dict[delta].append(node.value)
		else:
			order_dict[delta] = [node.value]
		if node.left:
			diff = delta - 1
			nx = diff if diff < nx else nx
			q.append((node.left, diff))
		if node.right:
			diff = delta + 1
			px = diff if diff > px else px
			q.append((node.right, diff))
	for i in range(nx, px+1):
		vertical_order += order_dict[i]
	return vertical_order

def zigzagtraversal(root):
	if not root:
		return []
	current_level = []
	next_level = []
	zigzag_traversal = []
	current_level.append(root)
	while current_level:
		node = current_level.pop()
		zigzag_traversal.append(node.value)
		if node.left:
			next_level.append(node.left)
		if node.right:
			next_level.append(node.right)
		if not current_level:
			current_level = next_level
			next_level = []
	return zigzag_traversal

if __name__ == '__main__':
	t = BST()
	t.insert(50) 
	t.insert(30)
	t.insert(80)
	t.insert(70)
	t.insert(90)
	t.insert(85)
	t.insert(95)
	print("inorder: ", inorder(t.root))
	print("preorder: ", preorder(t.root))
	print("postorder: ", postorder(t.root))
	print("levelorder_recursive: ", levelorder_recursive(t.root))
	print("levelorder: ", levelorder(t.root))
	print("verticalorder: ", verticalorder(t.root))
	print("zigzagtraversal: ", zigzagtraversal(t.root))

	"""
				50

			30 		80
				70		90
			 		85		95
	"""