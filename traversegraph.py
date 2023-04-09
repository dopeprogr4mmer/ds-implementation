from  undirected_graph import Graph
from linkedlist import LinkedList

def dfs(G, v):
	tree = {}
	tovisit = [(None, v)]						#using list to implement stack

	while tovisit:
		a, b = tovisit.pop()
		if b not in tree:
			tree[b] = a 
			for neighbour in G.get_neighbours(b):					
				tovisit.append((b, neighbour))
				#tovisit.insert(0, (b,c))		# becomes BFS. Smooth! Inefficient tho :( [Queue reccomended]
	return tree

def bfs(G, v):
	tree = {}
	tovisit = LinkedList()						#using linkedlist to implement queue
	tovisit.append((None, v))
	
	while tovisit.head:
		a, b = tovisit.remove(tovisit.head.value)
		if b not in tree:
			tree[b] = a 
			for neighbour in G.get_neighbours(b):	
				tovisit.append((b, neighbour))
	print(tree)
	return tree 

def is_connected(G, u, v):
	return v in bfs(G, u)

def path(G, u, v):
	tree = dfs(G, v)
	if u in tree:
		path = []
		while u is not None:
			print(u)
			path.append(u)
			u = tree[u]
		return path


if __name__ == '__main__':
	G = Graph([], 'ab bc cd ad bd de ef gh ax'.split())
	print(dfs(G, 'a'))
	assert(is_connected(G, 'a', 'f'))
	assert(not is_connected(G, 'f', 'g'))
	print(path(G, 'b', 'f'))
