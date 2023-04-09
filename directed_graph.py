"""
Implementation of a uni-directed unweighted graph [adjacency matrix]
"""

import pprint

class Graph:
	def __init__(self, n):
		self.graph = [[0 for x in range(n)] for y in range(n)]
		self.size = n

	def print_graph(self):
		pprint.pprint(self.graph)	

	def add_edge(self, x, y):
		self.graph[x][y]=1
 	
	def BFS(self, vertex, visited=[], q=[]):
		visited.append(vertex)
		for neighbour in range(self.size):
			edge = self.graph[vertex][neighbour]
			if edge:
				if neighbour not in visited and neighbour not in q:
					q.append(neighbour)
		while q:
			next_vertex = q.pop(0)
			self.BFS(next_vertex, visited, q)
		return visited
		
	def DFS(self, vertex, visited=[]):
		visited.append(vertex)
		for neighbour in range(self.size):
			edge = self.graph[vertex][neighbour]
			if edge:
				if neighbour not in visited:
					self.DFS(neighbour, visited)
		return visited
		
	def is_cyclic(self, vertex, visited=set()):
		if vertex in visited:
			return True
		if len(visited)==self.size:
			return False
		visited.add(vertex)
		for neighbour in range(self.size):
			edge = self.graph[vertex][neighbour]
			if edge:
				if neighbour not in visited:
					return self.is_cyclic(neighbour, visited)
		return True

	def is_disconnected(self, fn):
		visited=[]
		fn(0, visited)
		if len(visited) != self.size:
			return True
		return False
					
g = Graph(7)
g.add_edge(0,1)
g.add_edge(0,5)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(5,6)
g.add_edge(6,4)
g.print_graph()
print("BFS:", g.BFS(2))
print("DFS:", g.DFS(2))
print("Cyclic:", g.is_cyclic(0))
print("Disonnected", g.is_disconnected(g.BFS))