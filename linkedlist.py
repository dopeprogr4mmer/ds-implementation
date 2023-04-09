class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def get_head(self):
		return self.head

	def get_tail(self):
		return self.tail

	def get_length(self):
		return self.count

	def is_empty(self):
		if self.count == 0:
			return True
		return False

	def append(self, value):
		newnode = Node(value)
		if self.is_empty():
			self.head = newnode
		else:
			self.tail.next = newnode
		self.tail = newnode
		self.count += 1
		print('{} appended to end of LinkedList'.format(value))
		return True

	def insert(self, value, index):
		if index > self.get_length():
			print("Index out of range")
			return False
		if self.is_empty():
			self.append(value)
			return True
		i = 1
		newnode = Node(value)
		curr = self.get_head()
		while i < index:
			curr = curr.next
			i+=1
		curr.value, newnode.value = newnode.value, curr.value
		newnode.next = curr.next
		curr.next = newnode
		self.count += 1
		print("{} inserted to at index {}     -- 1 based indexing --".format(value, index))
		return True

	def remove(self, x):
		if self.is_empty():
			print('{} not in list'.format(x))
			return False
		head = self.get_head()
		curr = head
		prev = None
		while curr:
			if curr.value == x:
				val = curr.value
				if curr == head:
					self.head = head.next
				elif curr.next != None:
					curr.value = curr.next.value
					curr.next = curr.next.next
				else:
					curr = None
					self.tail = prev
				self.count -= 1
				print('{} removed from list'.format(x))
				return val
			prev = curr
			curr = curr.next
		print('{} not in list'.format(x))
		return False
		
	def remove_recursive(self, x, curr=1, prev=None):
		if curr == 1:
			curr = self.get_head()
		if curr == None:
			print('{} not in list'.format(x))
			return False
		if curr.value == x:
			if curr == self.head:
				self.head = self.head.next
			elif curr.next != None:
				curr.value = curr.next.value
				curr.next = curr.next.next
			else:
				prev.next = None
				self.tail = prev
			self.count -= 1
			print('{} removed from list'.format(x))
			return True
		return self.remove_recursive(x, curr.next, curr)

	def reverse_in_place(self):
		self.tail = self.get_head()
		prev, curr, next_ = None, self.head, None 		# None --> p --> c --> n --> None
		while curr:
			next_ = curr.next
			curr.next = prev
			prev = curr 
			curr = next_
		self.head = prev

	def  __str__(self):
		selflist = []
		if self.is_empty():
			print("empty list")
			return []
		curr = self.get_head()
		while curr:
			selflist.append(curr.value)
			curr = curr.next
		return(str(selflist))
		
if __name__ == '__main__':
	linked_list = LinkedList()
	linked_list.append(2)
	linked_list.append(5)
	print(linked_list.get_length())
	print(linked_list)
	linked_list.insert(10, 1)		#1 based indexing
	print(linked_list)
	linked_list.remove_recursive(1)
	linked_list.remove_recursive(5)
	print(linked_list.get_length())
	print(linked_list)
	linked_list.append(100)
	linked_list.append(42)
	linked_list.append(23)
	linked_list.append(7)
	print(linked_list)
	linked_list.reverse_in_place()
	print(linked_list)
	linked_list.insert(102, 6)
	print(linked_list)
	linked_list.remove(10)
	print(linked_list)