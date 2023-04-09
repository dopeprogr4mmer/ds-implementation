"""
Implementation of a bi-directed unweighted graph [adjacency set]
"""

class Graph:
	def  __init__(self, V, E):
		self.E = set(frozenset((u,v)) for u, v in E)
		self._neighbours = {}
		for v in V:
			self.add_vertex(v)
		for u, v in E:
			self.add_edge(u,v)

	def add_vertex(self, v):
		if v not in self._neighbours:
			self._neighbours[v] = set()

	def add_edge(self, u, v):
		self.add_vertex(u)
		self.add_vertex(v)
		self.E.add(frozenset([u, v]))
		self._neighbours[u].add(v)
		self._neighbours[v].add(u)
   
	def remove_edge(self, u, v):
		e = frozenset([u,v])
		if e in self.E:
			self.E.remove(e)
			self._neighbours[u].remove(v)
			self._neighbours[v].remove(u)

	def remove_vertex(self, u):
		todelete = list(self.get_neighbours(u)) 
		for v in todelete:
			self.remove_edge(u, v)
		del self._neighbours[u]

	def get_degree(self, v):
		return len(self._neighbours[v])

	def get_neighbours(self, v):
		return iter(self._neighbours[v])


	@property
	def m(self):
		print(self.E)
		return len(self.E)

	@property
	def n(self):
		print(self._neighbours)
		return len(self._neighbours)
	

if __name__ == "__main__":
	G = Graph([1, 2, 3], {(1,2), (2,3)})	#can't have  set of sets/lists [unhashable type]
	assert(G.get_degree(1) == 1)
	assert(G.get_degree(2) == 2)
	assert(G.get_degree(3) == 1)

	assert(set(G.get_neighbours(2)) == {1,3})

	assert(G.n == 3 and G.m == 2)

	G.remove_edge(1, 2)
	assert(G.n == 3 and G.m == 1)

	# G.remove_edge(1, 3)
	# assert(G.n == 3 and G.m == 1)

	G.add_edge(1, 2)
	assert(G.n == 3 and G.m == 2)

	# G.remove_vertex(2)
	# assert(G.n ==2 and G.m == 0)

	G.add_vertex(4)
	G.add_edge(3, 4)
	G.m
	G.n