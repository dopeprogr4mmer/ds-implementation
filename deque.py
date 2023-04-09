class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None 

#Implementing Deque as a Doubly Linked List
class Deque:		
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def get_size(self):
		return self.size

	def append(self, data):
		new_node = Node(data) 
		if not self.head:
			self.head = new_node
			self.tail = new_node
			self.size += 1
			return
		self.tail.next = new_node
		new_node.prev = self.tail
		self.tail = new_node
		self.size += 1
		print("hi")
		return

	def appendleft(self, data):
		new_node = Node(data) 
		if not self.head:
			self.head = new_node
			self.tail = new_node
			self.size += 1
			return
		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node
		self.size += 1
		print("hi")
		return

	def pop(self):
		if not self.tail:
			return 
		data = self.tail.data
		if self.tail.prev:
			self.tail.prev.next = None 		#self.tail.next
			self.tail = self.tail.prev
		else:
			self.head = None
			self.tail = None
		self.size -= 1
		return data 

	def popleft(self):
		if not self.head:
			return 
		data = self.head.data
		if self.head.next:
			self.head.next.prev = None 		#self.head.prev
			self.head = self.head.next
		else:
			self.head = None
			self.tail = None
		self.size -= 1
		return data 

	def __str__(self):
		dll = []
		curr_node = self.head 
		while curr_node:
			dll.append(curr_node.data)
			curr_node = curr_node.next
		return str(dll)

#For insert and delete operations in middle of DLL
class DLL(Deque):
	def insert(self, data, index):		#1 based indexing
		if index > self.size:
			return 
		if index == 1:
			self.appendleft(data)
			return
		if index == self.size:
			self.append(data)
			return
		curr_node = self.head
		i = 1
		while i < index:
			curr_node = curr_node.next
			i += 1
		new_node = Node(data)
		curr_node.prev.next = new_node
		new_node.prev = curr_node.prev
		new_node.next = curr_node
		curr_node.prev = new_node
		if i == 1:
			self.head = new_node 
		self.size += 1
		return 

	def delete(self, index):	#1 based indexing
		if index>self.size:
			return False
		if index == self.size:
			return self.pop()
		if index == 1:
			return self.popleft()
		i = 1
		while i < index:
			curr_node = curr_node.next
			i += 1
		curr_node.prev.next = curr_node.next
		curr_node.next.prev = curr_node.prev
		if i == 1:
			self.head = new_node 
		self.size -= 1
		return 

if __name__ == '__main__':
	dll = DLL()
	dll.append(2)
	dll.popleft()
	print(dll)
	print(dll.head)
	print(dll.tail)
	dll.appendleft(5)
	dll.append(7)
	dll.appendleft(11)
	print(dll)
	print(dll.head.data)
	print(dll.tail.data)
	dll.append(9)
	print(dll)
	dll.popleft()
	print(dll)
	print(dll.head.data)
	print(dll.tail.data)
	dll.pop()
	print(dll)
	print(dll.head.data)
	print(dll.tail.data)
	dll.insert(10, 2)
	print(dll)
	print(dll.head.data)
	print(dll.tail.data)
	dll.delete(3)
	print(dll)
	print(dll.head.data)
	print(dll.tail.data)