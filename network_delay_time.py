import heapq 
from collections import defaultdict

"""
When you put the objects (i.e. tuples) into heap, 
it will take the first attribute in the object (in this case is key) to compare. 
If a tie happens, the heap will use the next attribute (i.e. value_1) and so on.
"""

class Solution:
	def get_max_delay(self, times: list[list[int]], n: int, k: int) -> int:
		edges = defaultdict(list)
		for u, v, w in times:
			edges[u].append((v, w))
		min_heap = [(0, k)]
		visited = set()
		time = 0
		while min_heap:
			w1, v1 = heapq.heappop(min_heap)
			if v1 in visited:
				continue
			visited.add(v1)
			time = max(time, w1)
			for v2, w2 in edges[v1]:
				if v2 not in visited:
					heapq.heappush(min_heap, (w1+w2, v2))
		return time if len(visited) == n else -1



if __name__ == '__main__':
	times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]] 
	n = 4
	k = 2
	s = Solution()
	max_delay = s.get_max_delay(times, n, k)
	print(max_delay)