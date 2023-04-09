from weighted_graph import Graph 
from collections import deque
import sys
import pprint
import time

def min_heapify(heap, i=0):
	n = len(heap)
	smallest = i
	left = (i * 2) + 1
	right = (i * 2) + 2
	if left<n and heap[left][1] < heap[smallest][1]:
		smallest = left
	if right<n and heap[right][1] < heap[smallest][1]:
		smallest = right 
	if smallest != i:
		heap[i], heap[smallest] = heap[smallest], heap[i]
		min_heapify(heap, smallest)


def get_shortest_path(graph):
	maxsize = 999	#sys.maxsize
	matrix = [[maxsize for j in range(len(graph.adjList))] for i in range(len(graph.adjList))] 
	#pprint.pprint(matrix)
	#print(unvisited)
	for v in range(len(graph.adjList)):
		visited = set()
		heap = deque()
		heap.append((v, 0))
		#flag = False
		while heap:
			#print(heap)
			s, w1 = heap.popleft()
			#print(v, s, w1)
			if s in visited:
				continue
			visited.add(s)
			if w1 < matrix[v][s]:
				matrix[v][s] = w1
				#flag = True
			for d, w2 in graph.adjList[s]:
				if d not in visited:
					if w2 < matrix[s][d]:
						matrix[s][d] = w2
						#flag = True
					#matrix[s][d] = min(matrix[s][d], w2)
					heap.appendleft((d, w1+w2))
					min_heapify(heap)
				#print(d, w2, )
		#
		#pprint.pprint(matrix)
		# break
	#pprint.pprint(matrix)
	return(matrix)


if __name__ == '__main__':
	edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10), (4, 5, 4), (5, 4, 1), (3, 4, 8), (1, 3, 7), (2, 5, 2)]
	n = 6
	graph = Graph(edges, n) 
	shortest_path = get_shortest_path(graph)
	pprint.pprint(shortest_path)

#O(E * log(V))