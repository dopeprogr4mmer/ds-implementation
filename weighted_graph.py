"""
Implementation of a uni-directed weighted graph [adjacency list]
"""

class Graph:
	def __init__(self, edges, n):
		self.adjList = [[] for _ in range(n)]

		for (src, dest, weight) in edges:
			self.adjList[src].append((dest, weight))

	def print_graph(self):
		for src in range(len(self.adjList)):
			print(src, self.adjList[src])
			# for dest, weight in self.adjList[src]:
			# 	print(f'{src} --> {dest}, {weight}')
			# print()

if __name__ == '__main__':
    # Input: Edges in a weighted digraph (as per the above diagram)
    # Edge (x, y, w) represents an edge from `x` to `y` having weight `w`
    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
            (4, 5, 1), (5, 4, 3)]
 
    # No. of vertices (labelled from 0 to 5)
    n = 6
 
    # construct a graph from a given list of edges
    graph = Graph(edges, n)
 
    # print adjacency list representation of the graph
    graph.print_graph() 