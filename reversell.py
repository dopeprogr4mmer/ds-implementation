def reverse(self):
	prev_node, curr_node, next_node = None, self, None
	while curr_node:
		next_node = curr_node.next
		curr_node.next = prev_node
		prev_node = curr_node
		curr_node = next_node
	return prev_node

def reverse_recursive(curr=1, prev=None):
	if curr == 1:
		curr = self
	next_ = curr.next
	curr.next = prev
	if not next_:
		return curr 
	return next_.reverse_recursive(curr)

def reverse_in_groups(curr=1, k):
	c = 0
	if curr == 1:
		head = self
	head = curr
	prev_node, curr_node, next_node = None, head, None
	while curr_node and c<k:
		next_node = curr_node.next
		curr_node.next = prev_node
		prev_node = curr_node
		curr_node = next_node
		c+=1
	if curr_node:
		head.next = reverse_in_groups(curr, k)
	return prev_node