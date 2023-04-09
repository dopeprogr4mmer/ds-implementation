def topview(self):
	q = deque()
	#tv[0]=self.value
	if self.is_empty():
		return []
	else:
		q.append((0, self))
	def view(q, tv={}):
		if not q:
			return tv
		x = q.popleft()
		index, node = x[0], x[1]
		if not index in tv.keys():
			tv[index]=node.value
			#print(tv)
		if not node.left.is_empty():
			q.append((index-1, node.left))
		if not node.right.is_empty():
			q.append((index+1, node.right))
		return view(q, tv)
	view_dict = view(q)
	#print(x)
	top_view = sorted(view_dict.items(), key=lambda x: x[0])
	#print(x)
	top_view = [i[1] for i in top_view]
	return top_view

def bottomview(self):
	if self.is_empty():
		return []
	q = deque()
	q.append((0, self))
	def view(q, bv={}):
		"""If there are multiple bottom-most nodes 
		for a horizontal distance from root, 
		then print the later one in level traversal"""
		if not q:
			return bv
		z = q.popleft()
		index, node = z[0], z[1]
		#if not index in bv:			#diff bw top/bottom view
		bv[index] = node.value
		if not node.left.is_empty():
			q.append((index-1, node.left))
		if not node.right.is_empty():
			q.append((index+1, node.right))
		return view(q, bv)
	view_dict = view(q)
	bottom_view = sorted(view_dict.items(), key=lambda x: x[0])
	print(bottom_view)
	bottom_view = [i[1] for i in bottom_view]
	print(bottom_view)

def leftview(self):
	if self.is_empty():
		return []
	depth, shift = 0, 0
	q = deque()
	q.append((depth, shift, self))
	def view(q, lv={}):
		#print(lv)
		if not q:
			return lv
		y = q.pop()
		depth, shift, node = y[0], y[1], y[2]
		if depth in lv.keys():
			if shift<lv[depth][0]:				#> for rightview
				lv[depth]=(shift, node.value)
		else:
			lv[depth]=(shift, node.value)
		if not node.left.is_empty():
			q.append((depth+1, shift-1, node.left))
		if not node.right.is_empty():
			q.append((depth+1, shift+1, node.right))
		return view(q, lv)
	view_dict = view(q)
	#print(view_dict)
	left_view = [view_dict[z] for z in view_dict]
	#print(left_view)
	left_view = [i[1] for i in left_view]
	return left_view

def left_view_dfs(self, level=1, max_level=[0]):
	if self.is_empty():
		return 
	if max_level[0]<level:
		print(self.value)
		#return_list.append(self.value)
		max_level[0]=level
	self.left.left_view_dfs(level+1, max_level)
	self.right.left_view_dfs(level+1, max_level)